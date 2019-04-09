#!/bin/sh

set -e

if [ $# -ne 1 ]; then

  printf "\n%s\n\n" " >>> ERROR -- one input argument required (path to output directory)"
  exit 1
fi

OUTPUT_DIR="$1"

if [ -d ${OUTPUT_DIR} ]; then

  printf "\n%s\n\n" " >>> ERROR -- target output directory already exists: ${OUTPUT_DIR}"
  exit 1
fi

mkdir -p ${OUTPUT_DIR}
cd       ${OUTPUT_DIR}

#EDM_INPUT=/store/relval/CMSSW_10_6_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_105X_upgrade2018_realistic_v6-v1/10000/B82E4EBC-7E5F-314C-B7BE-B44C418F244A.root
DAS_SAMPLE=/RelValTTbar_13/CMSSW_10_6_0_pre2-PUpmx25ns_105X_upgrade2018_realistic_v6-v1/GEN-SIM-RECO

dasgoclient --query "file dataset=${DAS_SAMPLE}" > inputs.txt

OUTPUT_TAG=RelValTTbar_13_CMSSW_10_6_0_pre2-PUpmx25ns_105X_upgrade2018_realistic_v6

STEP1_OUTPUT=${OUTPUT_TAG}_DQM.root
STEP1_CFG_PY=${OUTPUT_TAG}_DQM_cfg.py
STEP2_CFG_PY=${OUTPUT_TAG}_Harvesting_cfg.py

# --- Step_1: DQM
if [ ! -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step1 \
   --step DQM:offlineHLTSource4physicsPD \
   --filein  filelist:inputs.txt \
   --fileout         ${STEP1_OUTPUT} \
   --python_filename ${STEP1_CFG_PY} \
   --mc \
   --eventcontent DQM \
   --datatier DQMIO \
   --conditions auto:phase1_2018_realistic \
   --era Run2_2018 \
   --geometry DB:Extended \
   --nThreads 1 \
   --no_exec \
   --runUnscheduled \
   --customise Configuration/DataProcessing/Utils.addMonitoring \
   -n -1 || exit $? ;

  cmsRun ${STEP1_CFG_PY}

else

  printf "\n%s\n\n" " >>> WARNING -- skipped Step_1 , target output file already exists: ${STEP1_OUTPUT}"
fi

# --------------

# --- Step_2: Harvesting (output: DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root)

if [ -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step2 \
   --step HARVESTING:hltOfflineDQMClient --harvesting AtRunEnd \
   --filein     file:${STEP1_OUTPUT} \
   --python_filename ${STEP2_CFG_PY} \
   --filetype DQM \
   --mc \
   --scenario pp \
   --conditions auto:phase1_2018_realistic \
   --era Run2_2018 \
   --geometry DB:Extended \
   --no_exec \
   -n -1 || exit $? ;

  cmsRun ${STEP2_CFG_PY}

else

  printf "\n%s\n\n" " >>> WARNING -- skipped Step_2 , target input file not found: ${STEP1_OUTPUT}"
fi

# --------------

#unset -v EDM_INPUT
unset -v DAS_SAMPLE
unset -v OUTPUT_DIR
unset -v OUTPUT_TAG
unset -v STEP1_OUTPUT
unset -v STEP1_CFG_PY
unset -v STEP2_CFG_PY

#!/bin/sh

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

AOD_INPUT=/store/mc/RunIIAutumn18DRPremix/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/270000/87EF3D51-5441-2F49-A2BC-54C446667ACD.root

OUTPUT_TAG=ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8

STEP1_OUTPUT=${OUTPUT_TAG}_DQM.root
STEP1_CFG_PY=${OUTPUT_TAG}_DQM_cfg.py
STEP2_CFG_PY=${OUTPUT_TAG}_Harvesting_cfg.py

# --- Step_1: DQM
if [ ! -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step1 \
   --step DQM:offlineValidationHLTSourceOnAOD \
   --filein ${AOD_INPUT} \
   --fileout    file:${STEP1_OUTPUT} \
   --python_filename ${STEP1_CFG_PY} \
   --mc \
   --eventcontent DQM \
   --datatier DQMIO \
   --conditions 102X_upgrade2018_realistic_v15 \
   --geometry DB:Extended \
   --era Run2_2018 \
   --nThreads 1 \
   --no_exec \
   --runUnscheduled \
   --customise Configuration/DataProcessing/Utils.addMonitoring \
   -n 1000 || exit $? ;

  cmsRun ${STEP1_CFG_PY}

else

  printf "\n%s\n\n" " >>> WARNING -- skipped Step_1 , target output file already exists: ${STEP1_OUTPUT}"
fi

# --------------

# --- Step_2: Harvesting (output: DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root)

if [ -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step2 \
   --step HARVESTING:dqmHarvesting --harvesting AtRunEnd \
   --filein     file:${STEP1_OUTPUT} \
   --python_filename ${STEP2_CFG_PY} \
   --filetype DQM \
   --mc \
   --scenario pp \
   --conditions 102X_upgrade2018_realistic_v15 \
   --geometry DB:Extended \
   --era Run2_2018 \
   --no_exec \
   -n -1 || exit $? ;

  cmsRun ${STEP2_CFG_PY}

else

  printf "\n%s\n\n" " >>> WARNING -- skipped Step_2 , target input file not found: ${STEP1_OUTPUT}"
fi

# --------------

unset -v AOD_INPUT
unset -v OUTPUT_DIR
unset -v OUTPUT_TAG
unset -v STEP1_OUTPUT
unset -v STEP1_CFG_PY
unset -v STEP2_CFG_PY

#!/bin/sh

set -e

if [ $# -ne 1 ]; then

  echo " >>> specify one command-line argument: year (must be 2016, 2017, or 2018)"
  exit 1;
fi

YEAR=${1}

if [ ${YEAR} == 2016 ]; then

  # Run2016
  LUMISEC_JSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
  NORM_TAG=/cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json

  HLT_PATHS=(

    HLT_PFHT300_PFMET110_v
    HLT_PFMET300_v
    HLT_PFMET120_PFMHT120_IDTight_v
    HLT_PFMET170_HBHECleaned_v
    HLT_MET200_v

    HLT_PFMET110_v
    HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v
  )
  ### ----------

elif [ ${YEAR} == 2017 ]; then

  # Run2017
  LUMISEC_JSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
  NORM_TAG=/cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json

  HLT_PATHS=(

    HLT_PFHT500_PFMET100_PFMHT100_IDTight_v
    HLT_PFHT700_PFMET85_PFMHT85_IDTight_v
    HLT_PFHT800_PFMET75_PFMHT75_IDTight_v
    HLT_PFMET120_PFMHT120_IDTight_v
    HLT_PFMET250_HBHECleaned_v
  )
  ### ----------

elif [ ${YEAR} == 2018 ]; then

  # Run2018
  LUMISEC_JSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt
  NORM_TAG=/cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json

  HLT_PATHS=(

    HLT_PFHT500_PFMET100_PFMHT100_IDTight_v
    HLT_PFHT700_PFMET85_PFMHT85_IDTight_v
    HLT_PFHT800_PFMET75_PFMHT75_IDTight_v
    HLT_PFMET120_PFMHT120_IDTight_v
    HLT_PFMET120_PFMHT120_IDTight_PFHT60_v
    HLT_PFMET200_HBHE_BeamHaloCleaned_v
    HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v
    HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v
    HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v
  )
  ### ----------

else

  echo " >>> invalid year: ${1}"
  exit 1;
fi

### ----------

OUTDIR=outputs_brilcalc_${YEAR}

mkdir -p ${OUTDIR}

brilcalc lumi -u /fb --normtag ${NORM_TAG} -i ${LUMISEC_JSON} > ${OUTDIR}/brilcalc_Run${YEAR}.txt
echo "done: ${OUTDIR}/brilcalc_Run${YEAR}.txt"

for hlt_path in "${HLT_PATHS[@]}"; do

  brilcalc lumi -u /fb --normtag ${NORM_TAG} -i ${LUMISEC_JSON} --hltpath "${hlt_path}*" > ${OUTDIR}/brilcalc_Run${YEAR}_${hlt_path}.txt
  echo "done: ${OUTDIR}/brilcalc_Run${YEAR}_${hlt_path}.txt"

done
unset -v hlt_path

### ----------

unset -v YEAR OUTDIR LUMISEC_JSON NORM_TAG HLT_PATHS

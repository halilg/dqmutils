#!/bin/sh

if [ $# -ne 1 ]; then

  printf "\n%s\n\n" " >>> ERROR -- one input argument required (path to input directory)"
  exit 1
fi

INPUT_DIR="$1"

OUTPUT_DIR=${INPUT_DIR}/plots

if [ -d ${OUTPUT_DIR} ]; then

  printf "\n%s\n\n" " >>> ERROR -- target output directory already exists: ${OUTPUT_DIR}"
  exit 1
fi

INPUT_FILE=DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

if [ -f ${INPUT_DIR}/${INPUT_FILE} ]; then

  ./plot_DQMHistos.py -i ${INPUT_DIR}/${INPUT_FILE} -o ${OUTPUT_DIR} -e png --only-keys '/HLT/' '/TOP/'

else

  printf "\n%s\n\n" " >>> WARNING -- no action taken, target input file not found: ${INPUT_DIR}/${INPUT_FILE}"
fi

unset -v INPUT_DIR
unset -v OUTPUT_DIR
unset -v INPUT_FILE

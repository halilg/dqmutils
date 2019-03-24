#!/bin/sh

INPUT_FILE=DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

OUTPUT_DIR=tmp

if [ -f ${INPUT_FILE} ]; then

  ./plot_DQMHistos.py -i ${INPUT_FILE} -o ${OUTPUT_DIR} -e png --only-keys '/HLT/' '/TOP/'
fi

unset -v INPUT_FILE

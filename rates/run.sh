#!/bin/bash

#./hlt_nanoAOD.py -i nanoAOD_323755_EGamma/*.root --PD EGamma -o results_323755_EGamma.json --maxEvents 20000 #-r 323775 --lumi-min 52 --lumi-max 75

#for pd in EGamma SingleMuon DoubleMuon MuonEG; do
#
#  ./hlt_nanoAOD.py -i nanoAOD_323755_"${pd}"/*.root --PD "${pd}" -o results_323755_"${pd}".json -r 323775 --maxEvents 10000 #--lumi-min 52 --lumi-max 75
#
#done
#unset -v pd

for pd in DoubleMuon MuonEG; do

  ./hlt_nanoAOD.py -i nanoAOD_323755_"${pd}"/*.root --PD "${pd}" -o results_323755_"${pd}".json --maxEvents 10000 #--lumi-min 52 --lumi-max 75

done
unset -v pd

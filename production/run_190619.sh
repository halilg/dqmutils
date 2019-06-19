#!/bin/bash

set -e

sed -i 's|Color(1)|Color(4)|g' plot_DQMHistos_compare.py

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbar_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r RelValTTbar_13UP17/CMSSW_10_6_0_pre2-PUpmx25ns_105X_mc2017_realistic_v7_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'HLT:CMSSW_9_4_13_UL1 + RECO:CMSSW_10_6_0_pre2' \
 -o output_plots_190619_0L/1060_vs_1060pre2

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbarLepton_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r RelValTTbarLepton_13UP17/CMSSW_10_6_0_pre2-PUpmx25ns_105X_mc2017_realistic_v7_ulhlt17pmx_hs-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'HLT:CMSSW_9_4_13_UL1 + RECO:CMSSW_10_6_0_pre2' \
 -o output_plots_190619_1L/1060_vs_1060pre2

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbarLepton_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r RelValTTbarLepton_13UP17/CMSSW_10_6_0_pre2-PUpmx25ns_105X_mc2017_realistic_v7_ulhlt17pmx_hs-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'HLT:CMSSW_9_4_13_UL1 + RECO:CMSSW_10_6_0_pre2' \
 -o output_plots_190619_2L/1060_vs_1060pre2

git co -- plot_DQMHistos_compare.py

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbar_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'Fall17 (94X)' \
 -o output_plots_190619_0L/1060_vs_Fall17

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbarLepton_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r TTToSemiLeptonic_TuneCP5down_RunIIFall17DRPremix/Harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'Fall17 (94X)' \
 -o output_plots_190619_1L/1060_vs_Fall17

./plot_DQMHistos_compare.py -e png pdf --only-keys /HLT/ /TOP/ \
 -t RelValTTbarLepton_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 -r TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root \
 --t-leg 'HLT:CMSSW_9_4_14_UL + RECO:CMSSW_10_6_0' \
 --r-leg 'Fall17 (94X)' \
 -o output_plots_190619_2L/1060_vs_Fall17

# -t RelValTTbarLepton_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
#
# -t RelValTTbar_13UP17/CMSSW_10_6_0-PUpmx25ns_106X_mc2017_realistic_v3_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
# -r RelValTTbar_13UP17/CMSSW_10_6_0_pre2-PUpmx25ns_105X_mc2017_realistic_v7_ulhlt17hs_pmx-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
#
#
# -r TTToSemiLeptonic_TuneCP5down_RunIIFall17DRPremix/Harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
# -r TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
# -r TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

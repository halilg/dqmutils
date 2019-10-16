#!/bin/bash

OUTPUT_DIR=output_plots_191014_1064_106X_upgrade2018_realistic_v10

# ---

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'JME/' -e pdf png \
 -t RelValTTbar_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbar/JetMET_DQM

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -t RelValTTbar_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbar

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbar_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbar/GeneralHLTOfflineTEST

./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbar_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbar/GeneralHLTOfflineTEST_eff

# ---

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbarLepton

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbarLepton/GeneralHLTOfflineTEST

./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/*.root \
 --t-leg 'CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o ${OUTPUT_DIR}/1064_vs_1025/RelValTTbarLepton/GeneralHLTOfflineTEST_eff

# ---

unset -v OUTPUT_DIR

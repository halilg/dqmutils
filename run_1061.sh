#!/bin/bash

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -t RelValTTbar_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbar

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbar_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbar/GeneralHLTOfflineTEST

./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbar_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbar_13/CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbar/GeneralHLTOfflineTEST_eff

# ---

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbarLepton

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbarLepton/GeneralHLTOfflineTEST

./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1' \
 -r RelValTTbarLepton_13/CMSSW_10_2_5-PU25ns_102X_upgrade2018_realistic_v15_ECAL-v1/GEN-SIM-RECO_fixToGeneralHLTOffline/harvesting/*.root \
 --r-leg 'CMSSW_10_2_5-PUpmx25ns_102X_upgrade2018_realistic_v15_ECAL-v1' \
 -o output_plots_190822/1061_vs_1025/RelValTTbarLepton/GeneralHLTOfflineTEST_eff

# ---

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -t RelValTTbarLepton_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/FEVTDEBUGHLT_fixToGeneralHLTOffline/harvesting/*.root \
 --t-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1 [FEVTDEBUGHLT]' \
 -r RelValTTbarLepton_13UP18/CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1/DQMIO/harvesting/*.root \
 --r-leg 'CMSSW_10_6_1-PUpmx25ns_106X_upgrade2018_realistic_v6_ul18hlt_premix_hs-v1 [DQMIO]' \
 -o output_plots_190822/1061_FEVTDEBUGHLT_vs_DQMIO/RelValTTbarLepton

# ---

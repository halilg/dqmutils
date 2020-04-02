#!/bin/bash

OUTPUT_DIR=output_plots_UL16_v01

# ---

#./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
# -r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
# --r-leg 'TTbar RunIISummer16DR80Premix-PUMoriond17' \
# -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
# --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
# -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_80X/RelValTTbar/TOP_DQM
#
#./plot_DQMHistos_compare.py --only-keys 'HLT/' 'JME/' -e pdf png \
# -r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
# --r-leg 'TTbar RunIISummer16DR80Premix-PUMoriond17' \
# -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
# --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
# -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_80X/RelValTTbar/JetMET_DQM
#
#./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
# -r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
# --r-leg 'TTbar RunIISummer16DR80Premix-PUMoriond17' \
# -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
# --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
# -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_80X/RelValTTbar_GeneralHLTOfflineTEST/JetMET_DQM
#
#./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
# -r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
# --r-leg 'TTbar RunIISummer16DR80Premix-PUMoriond17' \
# -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
# --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
# -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_80X/RelValTTbar_GeneralHLTOfflineTEST_Eff/JetMET_DQM

# ---

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'TOP/' -e pdf png \
 -r RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
 --r-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
 -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/harvesting/*.root \
 --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_postVFP_v11' \
 -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_postVFP_v11/RelValTTbar/TOP_DQM

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'JME/' -e pdf png \
 -r RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
 --r-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
 -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/harvesting/*.root \
 --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_postVFP_v11' \
 -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_postVFP_v11/RelValTTbar/JetMET_DQM

./plot_DQMHistos_compare.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -r RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
 --r-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
 -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/harvesting/*.root \
 --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_postVFP_v11' \
 -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_postVFP_v11/RelValTTbar_GeneralHLTOfflineTEST/JetMET_DQM

./plot_DQMHistos_compare_GeneralHLTOffline.py --only-keys 'HLT/' 'GeneralHLTOfflineTEST/' -e pdf png root \
 -r RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/*.root \
 --r-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_preVFP_v5' \
 -t RelValTTbar_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/harvesting/*.root \
 --t-leg 'RelValTTbar CMSSW_10_6_8-PU25ns UL16hltval_postVFP_v11' \
 -o ${OUTPUT_DIR}/1068_UL16hltval_preVFP_v5_vs_postVFP_v11/RelValTTbar_GeneralHLTOfflineTEST_Eff/JetMET_DQM

# ---

unset -v OUTPUT_DIR

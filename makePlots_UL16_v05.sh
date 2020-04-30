#!/bin/bash

OUTPUT_DIR=output_plots_UL16_v06

# ---

./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/Filters/' -e pdf png \
-r TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
--r-leg 'RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6' --r-col 1 \
-t RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM/harvesting/*.root \
--t-leg 'CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP' --t-col 4 \
-o ${OUTPUT_DIR}/hltul16_postVFP_vs_80X/TTbar

#./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/Filters/' -e pdf png \
#-r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
#--r-leg 'RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6' --r-col 1 \
#-t RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM/harvesting/*.root \
#--t-leg 'CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP' --t-col 4 \
#-o ${OUTPUT_DIR}/hltul16_postVFP_vs_80X/TTbar

./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/Filters/' -e pdf png \
-r RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/AODSIM/harvesting/*.root \
--r-leg 'CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP' --r-col 2 \
-t RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM/harvesting/*.root \
--t-leg 'CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP' --t-col 4 \
-o ${OUTPUT_DIR}/hltul16_postVFP_vs_preVFP/TTbar

# ---

unset -v OUTPUT_DIR

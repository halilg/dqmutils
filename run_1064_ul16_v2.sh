#!/bin/bash

OUTPUT_DIR=output_plots_UL16_v02

# ---

#./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/GeneralHLTOfflineTEST/' -e pdf png \
# -r TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
# --r-leg 'TTbar RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1' --r-col 1 \
# -t RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/harvesting/*.root \
# --t-leg 'TTbarLepton CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1' --t-col 2 \
# -o ${OUTPUT_DIR}/10611cand3_hltul16_preVFP_vs_80X/RelValTTbarLepton_vs_TT

./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/GeneralHLTOfflineTEST/' -e pdf png \
 -r TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/*.root \
 --r-leg 'TTJets_SingleLeptFromT | RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016' --r-col 1 \
 -t RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/harvesting/*.root \
 --t-leg 'TTbarLepton | CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1' --t-col 2 \
 -o ${OUTPUT_DIR}/10611cand3_hltul16_preVFP_vs_80X/RelValTTbarLepton_vs_TT

./plot_DQMHistos_compare.py --only-keys '/HLT/Run summary/TOP/' '/HLT/Run summary/JME/' '/HLT/Run summary/GeneralHLTOfflineTEST/' -e pdf png \
 -r RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/harvesting/*.root \
 --r-leg 'TTbarLepton | CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1' --r-col 2 \
 -t RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM/harvesting/*.root \
 --t-leg 'TTbarLepton | CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1' --t-col 4 \
 -o ${OUTPUT_DIR}/10611cand3_hltul16_preVFP_vs_postVFP/RelValTTbarLepton_13UP16

# ---

unset -v OUTPUT_DIR

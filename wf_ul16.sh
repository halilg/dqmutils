
#./dqmJobs_driver.py -w AOD.MC.2016.0 --max-inputs 100 -d /QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM
# -o QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM -n 1000

#./dqmJobs_driver.py -w AOD.MC.2016.0 -d /RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM
# -o RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 -d /RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM
# -o RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM 

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
# -o QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting/
#
#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/*/*.root \
# -o RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM/harvesting/
#
#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/*/*.root \
# -o RelValQCD_FlatPt_15_3000HS_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM/harvesting/

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#--max-inputs 100 -n 1000 \
#-d /TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM \
#-o  TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM \
#-o  RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM \
#-o  RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
# -o TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
# -o TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/*/*.root \
# -o RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM/*/*.root \
# -o RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM/harvesting

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#--max-inputs 50 -n 5000 \
#-d /TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM \
#-o  TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hlt16-v1/AODSIM \
#-o  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hlt16-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_v12_hlt16post-v1/AODSIM \
#-o  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_v12_hlt16post-v1/AODSIM

#./dqmJobs_harvester.py -w MC.2016.0 \
#-i TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
#-o TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
#-i  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hlt16-v1/AODSIM/*/*.root \
#-o  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hlt16-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
#-i  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_v12_hlt16post-v1/AODSIM/*/*.root \
#-o  RelValTTbar_13UP16/CMSSW_10_6_11_CANDIDATE-PU25ns_106X_mcRun2_asymptotic_v12_hlt16post-v1/AODSIM/harvesting

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#--max-inputs 50 -n 5000 \
#-d /TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM \
#-o  TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/AODSIM \
#-o  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/AODSIM

#./dqmJobs_driver.py -w AOD.MC.2016.0 \
#-d /RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM \
#-o  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM

./dqmJobs_harvester.py -w MC.2016.0 \
-i  TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
-o  TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting

./dqmJobs_harvester.py -w MC.2016.0 \
-i  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/AODSIM/*/*.root \
-o  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/AODSIM/harvesting

./dqmJobs_harvester.py -w MC.2016.0 \
-i  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM/*/*.root \
-o  RelValTTbar_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/AODSIM/harvesting

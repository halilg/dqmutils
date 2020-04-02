
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

./dqmJobs_harvester.py -w MC.2016.0 \
 -i TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/*/*.root \
 -o TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/*/*.root \
# -o RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM/harvesting

#./dqmJobs_harvester.py -w MC.2016.0 \
# -i RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM/*/*.root \
# -o RelValTTbarLepton_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM/harvesting

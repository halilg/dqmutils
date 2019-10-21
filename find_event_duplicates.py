import ROOT

file0 = ROOT.TFile.Open('/pnfs/desy.de/cms/tier2/store/user/missirol/jme_trigger/jmeTriggerNtuples/191020/Data_Run2018D_SingleMuon_2/SingleMuon/crab_jmeTriggerNTuple_Data_Run2018D_SingleMuon_2/191020_185343/0000/Data_Run2018D_SingleMuon_1.root')

file1 = ROOT.TFile.Open('/pnfs/desy.de/cms/tier2/store/user/missirol/jme_trigger/jmeTriggerNtuples/191020/Data_Run2018D_SingleMuon_2/SingleMuon/crab_jmeTriggerNTuple_Data_Run2018D_SingleMuon_2/191020_185343/0000/Data_Run2018D_SingleMuon_1-1.root')

tree0 = file0.Get('JMETriggerNTuple/Events')
tree1 = file1.Get('JMETriggerNTuple/Events')

tree0.SetBranchStatus('*', False)
tree0.SetBranchStatus('event', True)
tree0.SetBranchStatus('run', True)
tree0.SetBranchStatus('luminosityBlock', True)
tree0.SetBranchStatus('event', True)

tree1.SetBranchStatus('*', False)
tree1.SetBranchStatus('run', True)
tree1.SetBranchStatus('luminosityBlock', True)
tree1.SetBranchStatus('event', True)

equal = 0

events0 = ['{:}:{:}:{:}'.format(i_evt.run, i_evt.luminosityBlock, i_evt.event) for i_evt in tree0]
events1 = ['{:}:{:}:{:}'.format(i_evt.run, i_evt.luminosityBlock, i_evt.event) for i_evt in tree1]

print list(set(events0).intersection(events1))

#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch()

tfile = ROOT.TFile.Open('QCD_Pt_170to300_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/AODSIM/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root')
histo_dc = {
  'HLT_PFJet080': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet80/effic_pfjetpT' , None,   2, 20, 'HLT_PFJet80'],
  'HLT_PFJet140': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet140/effic_pfjetpT', None,   4, 21, 'HLT_PFJet140'],
  'HLT_PFJet200': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet200/effic_pfjetpT', None,   6, 22, 'HLT_PFJet200'],
  'HLT_PFJet260': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet260/effic_pfjetpT', None,   8, 23, 'HLT_PFJet260'],
}
for key in histo_dc:
    h0 = tfile.Get(histo_dc[key][0])
    histo_dc[key][1] = h0.Clone()
    histo_dc[key][1].SetDirectory(0)
    histo_dc[key][1].SetLineColor(histo_dc[key][2])
    histo_dc[key][1].SetLineWidth(2)
    histo_dc[key][1].SetMarkerColor(histo_dc[key][2])
    histo_dc[key][1].SetMarkerSize(0.9)
    histo_dc[key][1].SetMarkerStyle(histo_dc[key][3])
tfile.Close()

tfile2 = ROOT.TFile.Open('RelValTTbar_13UP18/CMSSW_10_6_4_patch1-PUpmx25ns_106X_upgrade2018_realistic_v10-v1/FEVTDEBUGHLT/harvesting/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root')
histo2_dc = {
  'HLT_PFJet080': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet80/effic_pfjetpT' , None,   2, 24, 'HLT_PFJet80'],
  'HLT_PFJet140': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet140/effic_pfjetpT', None,   4, 25, 'HLT_PFJet140'],
  'HLT_PFJet200': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet200/effic_pfjetpT', None,   6, 26, 'HLT_PFJet200'],
  'HLT_PFJet260': ['DQMData/Run 1/HLT/Run summary/JME/Jets/AK4/PF/HLT_PFJet260/effic_pfjetpT', None,   8, 32, 'HLT_PFJet260'],
}
for key in histo2_dc:
    h0 = tfile2.Get(histo2_dc[key][0])
    histo2_dc[key][1] = h0.Clone()
    histo2_dc[key][1].SetDirectory(0)
    histo2_dc[key][1].SetLineColor(histo2_dc[key][2])
    histo2_dc[key][1].SetLineWidth(2)
    histo2_dc[key][1].SetMarkerColor(histo2_dc[key][2])
    histo2_dc[key][1].SetMarkerSize(0.9)
    histo2_dc[key][1].SetMarkerStyle(histo2_dc[key][3])
tfile2.Close()

canvas = ROOT.TCanvas('c','c', 500, 450)
canvas.SetLeftMargin(0.12)
canvas.SetTopMargin(0.10)
canvas.SetBottomMargin(0.12)
canvas.SetRightMargin(0.03)
hframe = canvas.DrawFrame(0, 0, 500, 1)
#hframe.SetTitle('QCD_Pt-170to300_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/AODSIM;jet p_{T} [GeV];Efficiency')
hframe.SetTitle(';Jet p_{T} [GeV];Efficiency')
#for key in sorted(histo2_dc.keys()):
#    histo2_dc[key][1].Draw('same,ep')
for key in sorted(histo_dc.keys()):
    histo_dc[key][1].Draw('same,ep')
#ROOT.gStyle.SetTitleSize(0.05)
hframe.GetXaxis().SetTitleSize(0.05)
hframe.GetYaxis().SetTitleSize(0.05)
hframe.GetXaxis().SetTitleOffset(1.1)
hframe.GetYaxis().SetTitleOffset(1.1)
hframe.GetXaxis().SetLabelSize(0.04)
hframe.GetYaxis().SetLabelSize(0.04)
canvas.Update()
leg = ROOT.TLegend(0.7, 0.2, 0.95, 0.6)
leg.SetBorderSize(1)
for key in sorted(histo_dc.keys()):
    leg.AddEntry(histo_dc[key][1], histo_dc[key][4], 'lep')
leg.Draw('same')
canvas.SaveAs('Run3Winter20DRPremixMiniAOD_QCD_Pt_170to300_14TeV_HLT_PFJet.pdf')
canvas.Close()

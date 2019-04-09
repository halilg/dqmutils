#!/usr/bin/env python
"""hlt_nanoAOD.py -- analyze HLT decisions in one NANOAOD file"""

import argparse, os, glob, json, ROOT

def KILL(log):
    raise RuntimeError(log)

def DecisionAndPurity(event, all_paths, paths):

    _pass = False
    _pure = False

#    cohe = False
#
#    for i_path in all_paths:
#        print getattr(evt, i_path), i_path
#        if getattr(evt, i_path): cohe = True
#
#    print '!'*100, cohe

    for i_path in paths:
        if hasattr(evt, i_path) and (getattr(evt, i_path) == 1): _pass = True; break;

    if _pass:

       _pure = True

       for i_path in all_paths:

           if i_path in paths: continue

           if hasattr(evt, i_path) and (getattr(evt, i_path) == 1): _pure = False; break;

    return _pass, _pure

#from HLTConfiguration import *
#HLT_paths = sorted(set(list(process.datasets.JetHT)))
#HLT_paths = [_tmp[:_tmp.rfind('_v')] for _tmp in HLT_paths]

HLT_paths = [

  'HLT_AK8PFHT750_TrimMass50',
  'HLT_AK8PFHT800_TrimMass50',
  'HLT_AK8PFHT850_TrimMass50',
  'HLT_AK8PFHT900_TrimMass50',
  'HLT_AK8PFJet140',
  'HLT_AK8PFJet15',
  'HLT_AK8PFJet200',
  'HLT_AK8PFJet25',
  'HLT_AK8PFJet260',
  'HLT_AK8PFJet320',
  'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17',
  'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1',
  'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2',
  'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4',
  'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02',
  'HLT_AK8PFJet360_TrimMass30',
  'HLT_AK8PFJet380_TrimMass30',
  'HLT_AK8PFJet400_TrimMass30',
  'HLT_AK8PFJet400',
  'HLT_AK8PFJet40',
  'HLT_AK8PFJet420_TrimMass30',
  'HLT_AK8PFJet450',
  'HLT_AK8PFJet500',
  'HLT_AK8PFJet550',
  'HLT_AK8PFJet60',
  'HLT_AK8PFJet80',
  'HLT_AK8PFJetFwd140',
  'HLT_AK8PFJetFwd15',
  'HLT_AK8PFJetFwd200',
  'HLT_AK8PFJetFwd25',
  'HLT_AK8PFJetFwd260',
  'HLT_AK8PFJetFwd320',
  'HLT_AK8PFJetFwd400',
  'HLT_AK8PFJetFwd40',
  'HLT_AK8PFJetFwd450',
  'HLT_AK8PFJetFwd500',
  'HLT_AK8PFJetFwd60',
  'HLT_AK8PFJetFwd80',
  'HLT_CaloJet500_NoJetID',
  'HLT_CaloJet550_NoJetID',
  'HLT_DiPFJetAve100_HFJEC',
  'HLT_DiPFJetAve140',
  'HLT_DiPFJetAve160_HFJEC',
  'HLT_DiPFJetAve200',
  'HLT_DiPFJetAve220_HFJEC',
  'HLT_DiPFJetAve260',
  'HLT_DiPFJetAve300_HFJEC',
  'HLT_DiPFJetAve320',
  'HLT_DiPFJetAve400',
  'HLT_DiPFJetAve40',
  'HLT_DiPFJetAve500',
  'HLT_DiPFJetAve60_HFJEC',
  'HLT_DiPFJetAve60',
  'HLT_DiPFJetAve80_HFJEC',
  'HLT_DiPFJetAve80',
  'HLT_DoublePFJets100_CaloBTagDeepCSV_p71',
  'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
  'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
  'HLT_DoublePFJets200_CaloBTagDeepCSV_p71',
  'HLT_DoublePFJets350_CaloBTagDeepCSV_p71',
  'HLT_DoublePFJets40_CaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
  'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
  'HLT_PFHT1050',
  'HLT_PFHT180',
  'HLT_PFHT250',
  'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5',
  'HLT_PFHT330PT30_QuadPFJet_75_60_45_40',
  'HLT_PFHT350MinPFJet15',
  'HLT_PFHT350',
  'HLT_PFHT370',
  'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94',
  'HLT_PFHT400_SixPFJet32',
  'HLT_PFHT430',
  'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59',
  'HLT_PFHT450_SixPFJet36',
  'HLT_PFHT500_PFMET100_PFMHT100_IDTight',
  'HLT_PFHT500_PFMET110_PFMHT110_IDTight',
  'HLT_PFHT510',
  'HLT_PFHT590',
  'HLT_PFHT680',
  'HLT_PFHT700_PFMET85_PFMHT85_IDTight',
  'HLT_PFHT700_PFMET95_PFMHT95_IDTight',
  'HLT_PFHT780',
  'HLT_PFHT800_PFMET75_PFMHT75_IDTight',
  'HLT_PFHT800_PFMET85_PFMHT85_IDTight',
  'HLT_PFHT890',
  'HLT_PFJet140',
  'HLT_PFJet15',
  'HLT_PFJet200',
  'HLT_PFJet25',
  'HLT_PFJet260',
  'HLT_PFJet320',
  'HLT_PFJet400',
  'HLT_PFJet40',
  'HLT_PFJet450',
  'HLT_PFJet500',
  'HLT_PFJet550',
  'HLT_PFJet60',
  'HLT_PFJet80',
  'HLT_PFJetFwd140',
  'HLT_PFJetFwd15',
  'HLT_PFJetFwd200',
  'HLT_PFJetFwd25',
  'HLT_PFJetFwd260',
  'HLT_PFJetFwd320',
  'HLT_PFJetFwd400',
  'HLT_PFJetFwd40',
  'HLT_PFJetFwd450',
  'HLT_PFJetFwd500',
  'HLT_PFJetFwd60',
  'HLT_PFJetFwd80',
  'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
  'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2',
  'HLT_QuadPFJet103_88_75_15',
  'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
  'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2',
  'HLT_QuadPFJet105_88_76_15',
  'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
  'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2',
  'HLT_QuadPFJet111_90_80_15',
  'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
  'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2',
  'HLT_QuadPFJet98_83_71_15',
  'HLT_Rsq0p35',
  'HLT_Rsq0p40',
  'HLT_RsqMR300_Rsq0p09_MR200_4jet',
  'HLT_RsqMR300_Rsq0p09_MR200',
  'HLT_RsqMR320_Rsq0p09_MR200_4jet',
  'HLT_RsqMR320_Rsq0p09_MR200',
  'HLT_SingleJet30_Mu12_SinglePFJet40',
]


#---

TTREE_KEY = 'Events'

#### main
if __name__ == '__main__':
   ### args
   parser = argparse.ArgumentParser(description=__doc__)

   parser.add_argument('-i', '--input', dest='input', action='store', default='', required=False,
                       help='path to input .root file (TopAnalysis NTuple under key "'+TTREE_KEY+'")')

   parser.add_argument('-o', '--output', dest='output', action='store', default='', required=False,
                       help='path to output text file')

#   parser.add_argument('-s', '--split', dest='split', action='store', type=int, default=1,
#                       help='split output into N separate cff.py files')
#
#   parser.add_argument('--das-client', dest='das_client', action='store', default='/cvmfs/cms.cern.ch/common/dasgoclient',
#                       help='path to das-client script (default: dasgoclient)')
#
#   parser.add_argument('--das-options', dest='das_opts',
##                      action='store', default='limit=0,key=~/.globus/userkey.pem,cert=~/.globus/usercert.pem',
#                       action='store', default='limit=0',
#                       help='comma-sep list of DAS query options')
#
#   parser.add_argument('--valid-only', dest='valid_only', action='store_true', default=False,
#                       help='skip data sets not in valid status')
#
#   parser.add_argument('-w', '--overwrite', dest='overwrite', action='store_true', default=False,
#                       help='overwrite output file(s)')

   opts, opts_unknown = parser.parse_known_args()
   ###

   ### --- configuration
   log_prx = os.path.basename(__file__)+' -- '

   VERBOSE = False

#   if not os.path.isfile(opts.input):
#      KILL(log_prx+'invalid path to input file [-i]: '+opts.input)

   if opts.output != '':

      if os.path.exists(opts.output):
         KILL(log_prx+'target path to output file already exists [-o]: '+opts.output)

   else:

      VERBOSE = True
   ### -----------------

   ### implementation --

   RUN = 319639
#   RUN = 320840

   MAX_EVENTS = -1 #1000000

#   INPUT_TFILE_PATHS = []
#   for _tmp in list(set(INPUT_FILES)): INPUT_TFILE_PATHS += ['root://cmsxrootd.fnal.gov/'+_tmp]

   INPUT_TFILE_PATHS = glob.glob('nanoAOD_'+str(RUN)+'/*.root')

#   INPUT_TREES = []
#
#   N_total = 0
#
#   for i_tfile_path in INPUT_TFILE_PATHS:
#
#       input_tfile = ROOT.TFile.Open(i_tfile_path)
#       if (not input_tfile) or input_tfile.IsZombie() or input_tfile.TestBit(ROOT.TFile.kRecovered): raise SystemExit(1)
#
#       input_ttree = input_tfile.Get(TTREE_KEY)
#       if not (input_ttree and input_ttree.InheritsFrom('TTree')):
#          KILL(log_prx+'input error: TTree key "writeNTuple/NTuple" not found in input file')
#
#       input_ttree.SetDirectory(0)
#
#       skimmed_tree = input_ttree.CopyTree('run=='+str(RUN))
#       skimmed_tree.SetDirectory(0)
#
#       input_tfile.Close()
#
#       INPUT_TREES += [skimmed_tree]
#
#       N_total += skimmed_tree.GetEntries()
#
#       print ' >>> added file:', i_tfile_path, '[events='+str(N_total)+']'
#
#   if len(INPUT_TREES) == 0:
#      KILL(log_prx+'input error: empty list input TTree objects')



#   if len(HLT_paths) == 0:
#
#      for i_branch_name in input_tchain.GetListOfBranches():
#
#          if str(i_branch_name.GetName()).startswith('HLT_'):
#
#             HLT_paths += [i_branch_name.GetName()]
#
#      HLT_paths = sorted(list(set(HLT_paths)))
#
#   print HLT_paths
#
#   print 'TTree['+TTREE_KEY+']::GetEntries() = '+str(N_total)

   ### ----------------------------------------------------------------------------------------------------

   pathGroup_paths = {

     'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94' : ['HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94'],
     'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59'       : ['HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59'],
     'HLT_PFHT350'                                     : ['HLT_PFHT350'],
     'HLT_PFHT450_SixPFJet36'                          : ['HLT_PFHT450_SixPFJet36'],
     'HLT_PFHT400_SixPFJet32'                          : ['HLT_PFHT400_SixPFJet32'],

     'Signal Paths': [

       'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94',
       'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59',
     ],

     'Control Paths': [

       'HLT_PFHT350',
       'HLT_PFHT450_SixPFJet36',
       'HLT_PFHT400_SixPFJet32',
     ],

     'Signal+Control Paths': [

       'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94',
       'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59',
       'HLT_PFHT350',
       'HLT_PFHT450_SixPFJet36',
       'HLT_PFHT400_SixPFJet32',
     ],
   }

   pathGroup_dict = {}

   for _tmp in pathGroup_paths.keys():
       pathGroup_dict.update({ _tmp : { 'paths': pathGroup_paths[_tmp], 'count_bare': 0, 'count_pure': 0, } })

   del pathGroup_paths

   ### ----------------------------------------------------------------------------------------------------

   lumiSections = []

   evt_N = 0

   for i_tfile_path in INPUT_TFILE_PATHS:

       input_tfile = ROOT.TFile.Open(i_tfile_path)
       if (not input_tfile) or input_tfile.IsZombie() or input_tfile.TestBit(ROOT.TFile.kRecovered): continue

       input_ttree = input_tfile.Get(TTREE_KEY)
       if not (input_ttree and input_ttree.InheritsFrom('TTree')):
          KILL(log_prx+'input error: TTree key "writeNTuple/NTuple" not found in input file')

       for i_branch in input_ttree.GetListOfBranches():

           i_branch_name = i_branch.GetName()

           branch_status = (i_branch_name in ['run', 'luminosityBlock']+HLT_paths)

           input_ttree.SetBranchStatus(i_branch_name, branch_status)

       print ' >>> added file:', i_tfile_path, '[events='+str(input_ttree.GetEntries())+']'

       break_file_loop = False

       for i_evt, evt in enumerate(input_ttree):

           if (i_evt % 100000) == 0: print i_evt

           if evt.run != RUN: continue

           if (evt_N % 100000) == 0: print '[', evt_N, ']'

           evt_N += 1

           if (MAX_EVENTS >= 0) and (evt_N > MAX_EVENTS): break_file_loop = True; break;

           if evt.luminosityBlock not in lumiSections: lumiSections += [evt.luminosityBlock]

           for i_pg in pathGroup_dict:

               hasPassed, isPure = DecisionAndPurity(event=evt, all_paths=HLT_paths, paths=pathGroup_dict[i_pg]['paths'])

               if hasPassed:

                  pathGroup_dict[i_pg]['count_bare'] += 1

                  if isPure: pathGroup_dict[i_pg]['count_pure'] += 1

       input_tfile.Close()

       if break_file_loop: break
   ### -----------------

   if len(lumiSections) != 0:

      TIME_SEC = len(set(lumiSections)) * 23.31

      # conversion from counts to Hz
      for _tmp in pathGroup_dict:
          pathGroup_dict[_tmp]['rate_bare'] = pathGroup_dict[_tmp]['count_bare'] / TIME_SEC
          pathGroup_dict[_tmp]['rate_pure'] = pathGroup_dict[_tmp]['count_pure'] / TIME_SEC

   print pathGroup_dict

   ### output ----------
   if opts.output != '':
      json.dump(pathGroup_dict, open(opts.output, 'w'), sort_keys=True, indent=2)
   ### -----------------

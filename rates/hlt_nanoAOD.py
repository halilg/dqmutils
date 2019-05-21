#!/usr/bin/env python
"""hlt_nanoAOD.py -- analyze HLT decisions in one NANOAOD file"""

import argparse, os, json, ROOT

LUMI_SECTION_TIME_SEC = 23.31

def KILL(log):
    raise RuntimeError(log)

def WARNING(log):
    print(' [WARNING] '+log)

def DecisionAndPurity(event, all_paths, paths):

    _pass = False
    _pure = False

    for i_path in paths:
        if hasattr(evt, i_path) and (getattr(evt, i_path) == 1): _pass = True; break;

    if _pass:

      _pure = True

      for i_path in all_paths:

           if i_path in paths: continue

           if hasattr(evt, i_path) and (getattr(evt, i_path) == 1): _pure = False; break;

    return _pass, _pure

### ----------------------------------------------------------------------------------------------------

#### main
if __name__ == '__main__':

   TTREE_KEY = 'Events'

   ### args
   parser = argparse.ArgumentParser(description=__doc__)

   parser.add_argument('-i', '--inputs', dest='inputs', nargs='+', default=[], required=True,
                       help='path to input NANOAOD file(s)')

   parser.add_argument('--PD', dest='PD', action='store', default=None, required=True,
                       help='name of Primary Dataset (PD) of input file(s)')

   parser.add_argument('-o', '--output', dest='output', action='store', default='', required=False,
                       help='path to output text file')

   parser.add_argument('-r', '--run', dest='run', action='store', default=None, required=False, type=int,
                       help='process only events in the specified Run')

   parser.add_argument('--lumi-min', dest='lumi_min', action='store', default=None, required=False, type=int,
                       help='process only events with "lumi-section >= lumi_min"')

   parser.add_argument('--lumi-max', dest='lumi_max', action='store', default=None, required=False, type=int,
                       help='process only events with "lumi-section <= lumi_max"')

   parser.add_argument('--maxEvents', dest='maxEvents', action='store', default=-1, required=False, type=int,
                       help='process only up to "maxEvents" events')

#   parser.add_argument('-w', '--overwrite', dest='overwrite', action='store_true', default=False,
#                       help='overwrite output file(s)')

   opts, opts_unknown = parser.parse_known_args()
   ###

   ### --- configuration
   log_prx = os.path.basename(__file__)+' -- '

   VERBOSE = False

   INPUT_TFILE_PATHS = sorted(list(set(opts.inputs)))

   if opts.output != '':

      if os.path.exists(opts.output):
         KILL(log_prx+'target path to output file already exists [-o]: '+opts.output)

   else:

      VERBOSE = True

   ### ----------------------------------------------------------------------------------------------------

   # EGamma
   if opts.PD == 'EGamma':

      pathGroup_paths = {

        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'],
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'   : ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'   ],

        'HLT_Ele27_WPTight_Gsf': ['HLT_Ele27_WPTight_Gsf'],
        'HLT_Ele28_WPTight_Gsf': ['HLT_Ele28_WPTight_Gsf'],
        'HLT_Ele30_WPTight_Gsf': ['HLT_Ele30_WPTight_Gsf'],
        'HLT_Ele32_WPTight_Gsf': ['HLT_Ele32_WPTight_Gsf'],
        'HLT_Ele35_WPTight_Gsf': ['HLT_Ele35_WPTight_Gsf'],
        'HLT_Ele38_WPTight_Gsf': ['HLT_Ele38_WPTight_Gsf'],
        'HLT_Ele40_WPTight_Gsf': ['HLT_Ele40_WPTight_Gsf'],

        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150'                    : ['HLT_Ele28_eta2p1_WPTight_Gsf_HT150'                    ],
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned': ['HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned'],

        'EleHT_OR_EleJet': [

          'HLT_Ele28_eta2p1_WPTight_Gsf_HT150',
          'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned',
        ],

        'Ele32_OR_EleHT': [

          'HLT_Ele32_WPTight_Gsf',
          'HLT_Ele28_eta2p1_WPTight_Gsf_HT150',
        ],

        'Ele32_OR_EleJet': [

          'HLT_Ele32_WPTight_Gsf',
          'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned',
        ],
      }

   # SingleMuon
   elif opts.PD == 'SingleMuon':

      pathGroup_paths = {
      
        'HLT_IsoMu24_eta2p1': ['HLT_IsoMu24_eta2p1'],
        'HLT_IsoMu24'       : ['HLT_IsoMu24'       ],
        'HLT_IsoMu27'       : ['HLT_IsoMu27'       ],
      }
      
   # MuonEG
   elif opts.PD == 'MuonEG':
      
      pathGroup_paths = {
      
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'],
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL'   : ['HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL'   ],
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'],
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'   : ['HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'   ],
      }
      
   # DoubleMuon
   elif opts.PD == 'DoubleMuon':
      
      pathGroup_paths = {
      
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8'],
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'  : ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'  ],
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'        : ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'        ],
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL'           : ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL'           ],
      }
      
   # JetHT
   elif opts.PD == 'JetHT':

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
   ### ----------------------------------------------------------------------------------------------------

   #### HLT Menu
   from Menu_HLT import *

   HLT_paths = []
   for _key in datasetMap:
       if opts.PD in datasetMap[_key]: HLT_paths += [_key]
   HLT_paths = sorted(list(set([_tmp[:_tmp.rfind('_v')] for _tmp in HLT_paths])))

   ### ----------------------------------------------------------------------------------------------------

   pathGroup_dict = {}

   for _tmp in pathGroup_paths.keys():
       pathGroup_dict.update({ _tmp : { 'paths': pathGroup_paths[_tmp], 'count_bare': 0, 'count_pure': 0, } })

   del pathGroup_paths

   ### ----------------------------------------------------------------------------------------------------

   runLumi_dict = {}

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

           if (i_evt != 0) and ((i_evt % 100000) == 0): print i_evt

           if (opts.run != None) and (evt.run != opts.run): continue

           if (opts.lumi_min != None) and (not (evt.luminosityBlock >= opts.lumi_min)): continue
           if (opts.lumi_max != None) and (not (evt.luminosityBlock <= opts.lumi_max)): continue

           if str(evt.run) not in runLumi_dict:
              runLumi_dict[str(evt.run)] = []

           if evt.luminosityBlock not in runLumi_dict[str(evt.run)]:
              runLumi_dict[str(evt.run)] += [evt.luminosityBlock]

           if (evt_N % 100000) == 0: print '[', evt_N, ']'

           evt_N += 1

           if (opts.maxEvents >= 0) and (evt_N > opts.maxEvents): break_file_loop = True; break;

           for i_pg in pathGroup_dict:

               hasPassed, isPure = DecisionAndPurity(event=evt, all_paths=HLT_paths, paths=pathGroup_dict[i_pg]['paths'])

               if hasPassed:

                  pathGroup_dict[i_pg]['count_bare'] += 1

                  if isPure: pathGroup_dict[i_pg]['count_pure'] += 1

       input_tfile.Close()

       if break_file_loop: break
   ### -----------------

   N_LUMI_SECTIONS = 0

   for key_run in runLumi_dict:

       runLumi_dict[key_run] = sorted(list(set(runLumi_dict[key_run])))

       N_LUMI_SECTIONS += len(runLumi_dict[key_run])

       runLumi_dict[key_run] = [[_tmp] for _tmp in runLumi_dict[key_run]]

   if N_LUMI_SECTIONS == 0:

      WARNING(log_prx+'empty of list of luminosity-sections, cannot determine rate values')

   else:

      TIME_SEC = N_LUMI_SECTIONS * LUMI_SECTION_TIME_SEC

      # conversion from counts to Hz
      for _tmp in pathGroup_dict:
          pathGroup_dict[_tmp]['rate_bare'] = pathGroup_dict[_tmp]['count_bare'] / TIME_SEC
          pathGroup_dict[_tmp]['rate_pure'] = pathGroup_dict[_tmp]['count_pure'] / TIME_SEC

   ### output ----------
   if opts.output != '':

      json.dump(pathGroup_dict, open(opts.output, 'w'), sort_keys=True, indent=2)

      json.dump(runLumi_dict, open(os.path.splitext(opts.output)[0]+'_lumis.json', 'w'), sort_keys=True, indent=2)
   ### -----------------

   print pathGroup_dict

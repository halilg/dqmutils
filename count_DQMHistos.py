#!/usr/bin/env python
import argparse
import os
import ROOT

from common import *

def get_keys(tdirectory, prefix='', contains_all=[], contains_one=[]):
    _keys = []

    for k_key in tdirectory.GetListOfKeys():
        k_key_name = k_key.GetName()
        k_obj = tdirectory.Get(k_key_name)
        if not k_obj: continue

        if k_obj.InheritsFrom('TDirectory'):
           _keys += get_keys(k_obj, prefix=prefix+k_obj.GetName()+'/', contains_all=contains_all, contains_one=contains_one)

        else: #if k_obj.InheritsFrom('TH1'):
           h_name = prefix+k_obj.GetName()

           if len(contains_all) > 0:
              skip = False
              for _tmp in contains_all:
                  if _tmp not in h_name: skip = True; break;
              if skip: continue

           if len(contains_one) > 0:
              skip = True
              for _tmp in contains_one:
                  if _tmp in h_name: skip = False; break;
              if skip: continue

           _keys += [prefix+k_obj.GetName()]

    return _keys

def increment_entry(dictionary, keys):
    if keys[0] not in dictionary: dictionary[keys[0]] = {'': 0}
    if len(keys) == 1: dictionary[keys[0]][''] += 1
    else: increment_entry(dictionary[keys[0]], keys[1:])

def get_total_count(dictionary):
    _n_total = 0
    for _tmp in sorted(dictionary.keys()):
        if isinstance(dictionary[_tmp], int):
           _n_total += dictionary[_tmp]
        elif isinstance(dictionary[_tmp], dict):
           _n_total += get_total_count(dictionary[_tmp])
    return _n_total

def printer(dictionary, label, levels, indent=''):
    _n_tot = get_total_count(dictionary)
    for _tmp in sorted(dictionary.keys()):
        if _tmp == '': print indent+label, '['+str(_n_tot)+']'
        elif isinstance(dictionary[_tmp], dict):
          if levels != 0:
             printer(dictionary[_tmp], label=_tmp, levels=levels-1, indent=indent+'  ')

#### main ----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    ### args --------------
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input', required=True, action='store', default=None,
                        help='path to input DQM .root file')

    parser.add_argument('-l', '--levels', dest='levels', action='store', type=int, default=-1,
                        help='show only first N levels of sub-directory (if negative, all levels are shown)')

    parser.add_argument('-k', '--keys-only', dest='keys_only', nargs='+', default=['/HLT/'],
                        help='list of strings required to be in histogram key')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    opts, opts_unknown = parser.parse_known_args()
    ### -------------------

    ROOT.gROOT.SetBatch()
    ROOT.gErrorIgnoreLevel = ROOT.kWarning

    log_prx = os.path.basename(__file__)+' -- '

    ### args validation ---
    if len(opts_unknown) > 0:
       KILL(log_prx+'unrecognized command-line arguments: '+str(opts_unknown))

    if not os.path.isfile(opts.input):
       KILL(log_prx+'invalid path to input .root file [-i]: '+opts.input)

    KEYS_ONLY = list(set(opts.keys_only))

    if opts.verbose and (len(KEYS_ONLY) > 0):
       print '\n >>> will plot only TH1 objects containing all of the following strings in their internal path:', KEYS_ONLY, '\n'
    ### -------------------

    # input file
    i_inptfile = ROOT.TFile.Open(opts.input)
    if (not i_inptfile) or i_inptfile.IsZombie() or i_inptfile.TestBit(ROOT.TFile.kRecovered): raise SystemExit(1)

    # list of keys inside TFile
    keys = get_keys(i_inptfile, contains_all=KEYS_ONLY)

    i_inptfile.Close()

    # dictionary of counts per directory
    hcount_dict = {'': 0}
    for _tmp in keys:
        _tmp_basename = os.path.basename(_tmp)
        _tmp_dirname = os.path.dirname(_tmp)
        _tmp_split = _tmp_dirname.split('/')
        increment_entry(hcount_dict, _tmp_split)

    # print out counters
    printer(hcount_dict, label='Total', levels=opts.levels)

#!/usr/bin/env python
import argparse, os, ROOT

from common import *

from plot_style import load_plot_style

def TH1_keys(tdirectory, prefix='', contains_all=[], contains_one=[]):

    th1_keys = []

    for k_key in tdirectory.GetListOfKeys():
        k_key_name = k_key.GetName()

        k_obj = tdirectory.Get(k_key_name)
        if not k_obj: continue

        if k_obj.InheritsFrom('TDirectory'):

           th1_keys += TH1_keys(k_obj, prefix=prefix+k_obj.GetName()+'/', contains_all=contains_all, contains_one=contains_one)

        elif k_obj.InheritsFrom('TH1'):

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

           th1_keys += [prefix+k_obj.GetName()]

    return th1_keys

def add_TH1_objects(filelist, contains_all):

    th1_dict = {}

    for i_inputf_path in filelist:

        i_inptfile = ROOT.TFile.Open(i_inputf_path)
        if (not i_inptfile) or i_inptfile.IsZombie() or i_inptfile.TestBit(ROOT.TFile.kRecovered): raise SystemExit(1)

        for h_key in TH1_keys(i_inptfile, contains_all=contains_all):

            if h_key in th1_dict:
               KILL(log_prx+'input error -> key "'+h_key+'" already exists in histogram-dictionary')

            h0 = i_inptfile.Get(h_key)
            if not (h0 and h0.InheritsFrom('TH1')):
               KILL(log_prc+'input error -- key "'+h_key+'" not associated to a TH1 object: '+opts.input)

            h_key_dict = '/'.join(h_key.split('/')[2:])

            if h_key_dict in th1_dict: th1_dict[h_key_dict].Add(h0)
            else                     : th1_dict[h_key_dict] =   h0.Clone(); th1_dict[h_key_dict].SetDirectory(0);

            if opts.verbose: print '\033[1m'+'\033[92m'+'[input]'+'\033[0m', h_key

        ROOT.gROOT.GetListOfFiles().Remove(i_inptfile)
        i_inptfile.Close()

    return th1_dict
#### ----

#### main
if __name__ == '__main__':
    ### args --------------
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--target', dest='target', required=True, nargs='+', default=[],
                        help='path to input DQM .root file')

    parser.add_argument('-r', '--reference', dest='reference', required=True, nargs='+', default=[],
                        help='path to input DQM .root file')

    parser.add_argument('--only-keys', dest='only_keys', nargs='+', default=[],
                        help='list of strings required to be in histogram key')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    opts, opts_unknown = parser.parse_known_args()
    ### -------------------

    ROOT.gROOT.SetBatch()
    ROOT.gErrorIgnoreLevel = ROOT.kWarning

    log_prx = os.path.basename(__file__)+' -- '

    ### args validation ---
    ONLY_KEYS = list(set(opts.only_keys))

    if len(ONLY_KEYS):
       print '\n >>> will plot only TH1 objects containing all of the following strings in their internal path:', ONLY_KEYS, '\n'

    if len(opts_unknown) > 0:
       KILL(log_prx+'unrecognized command-line arguments: '+str(opts_unknown))
    ### -------------------

    ### input histograms --
    histo_dict_target = add_TH1_objects(filelist=opts.target, contains_all=ONLY_KEYS)
    histo_dict_refern = add_TH1_objects(filelist=opts.reference, contains_all=ONLY_KEYS)

    ### comparisons
    histonames = sorted(list(set(histo_dict_target.keys() + histo_dict_refern.keys())))

    for h_key in histonames:

        if h_key not in histo_dict_target:
           print h_key, opts.verbose*' a'
           continue

        elif h_key not in histo_dict_refern:
           print h_key, opts.verbose*' b'
           continue

        else:
           h0 = histo_dict_refern[h_key]
           h1 = histo_dict_target[h_key]

           if h0.GetEntries() != h1.GetEntries():
              print h_key, opts.verbose*' c', '[entries =', h0.GetEntries(), ',', h1.GetEntries(), '] [nbins =', h0.GetNbinsX(), h1.GetNbinsX(), ']'
              continue

           elif h0.GetNbinsX() != h1.GetNbinsX():
              print h_key, opts.verbose*' d'
              continue

           elif h0.GetNbinsY() != h1.GetNbinsY():
              print h_key, opts.verbose*' e'
              continue

           elif h0.GetNbinsZ() != h1.GetNbinsZ():
              print h_key, opts.verbose*' f'
              continue

           else:
              h0_nbins = h0.GetNbinsX() * h0.GetNbinsY() * h0.GetNbinsZ()

              for i_bin in range(h0_nbins+2):
                  i_val0 = h0.GetBinContent(i_bin)
                  i_val1 = h1.GetBinContent(i_bin)

                  if i_val0 != i_val1:
                     print h_key, opts.verbose*' g'
                     break

                  i_err0 = h0.GetBinError(i_bin)
                  i_err1 = h1.GetBinError(i_bin)

                  if i_err0 != i_err1:
                     print h_key, opts.verbose*' h'
                     break

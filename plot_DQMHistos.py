#!/usr/bin/env python
import argparse, os, ROOT

from common import *

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
#### ----

#### main
if __name__ == '__main__':
    ### args --------------
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input', required=True, action='store', default=None,
                        help='path to input DQM .root file')

    parser.add_argument('-o', '--output', dest='output', required=True, action='store', default=None,
                        help='path to output directory')

    parser.add_argument('--only-keys', dest='only_keys', nargs='+', default=[],
                        help='list of strings required to be in histogram key')

    parser.add_argument('-e', '--exts', dest='exts', nargs='+', default=['png'],
                        help='list of extension(s) for output file(s)')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    opts, opts_unknown = parser.parse_known_args()
    ### -------------------

    ROOT.gROOT.SetBatch()
    ROOT.gErrorIgnoreLevel = ROOT.kWarning

    log_prx = os.path.basename(__file__)+' -- '

    ### args validation ---
    if not os.path.isfile(opts.input):
       KILL(log_prx+'invalid path to input .root file [-i]: '+opts.input)

    if os.path.exists(opts.output):
       KILL(log_prx+'target path to output .root file already exists [-o]: '+opts.output)

    EXTS = list(set(opts.exts))

    ONLY_KEYS = list(set(opts.only_keys))
    ### -------------------

    ### input histograms --
    histo_dict = {}

    i_inptfile = ROOT.TFile.Open(opts.input)
    if (not i_inptfile) or i_inptfile.IsZombie() or i_inptfile.TestBit(ROOT.TFile.kRecovered): raise SystemExit(1)

    for h_key in TH1_keys(i_inptfile, contains_all=ONLY_KEYS):

        if h_key in histo_dict:
           KILL(log_prx+'input error -> key "'+h_key+'" already exists in histogram-dictionary')

        h0 = i_inptfile.Get(h_key)
        if not (h0 and h0.InheritsFrom('TH1')):
           KILL(log_prc+'input error -- key "'+h_key+'" not associated to a TH1 object: '+opts.input)

        h0.SetDirectory(0)
        histo_dict[h_key] = h0

        if opts.verbose: print '\033[1m'+'\033[92m'+'[input]'+'\033[0m', h_key

    i_inptfile.Close()
    ### -------------------

    ### output files (plots)
    for histo_key in sorted(histo_dict.keys()):

        canvas = ROOT.TCanvas(histo_key, histo_key)
#        canvas.SetGrid(1,1)
#        canvas.SetTickx()
#        canvas.SetTicky()

        if histo_dict[histo_key].InheritsFrom('TH3'):

           WARNING(log_prx+'input histogram inherits from TH3 (not supported), will be skipped')
           continue

        elif histo_dict[histo_key].InheritsFrom('TH2'):

           h_draw_opt = 'colz,text'

        else:

           h_draw_opt = 'hist,e0'

        canvas.cd()
        histo_dict[histo_key].Draw(h_draw_opt)

        output_basename_woExt = os.path.abspath(opts.output)+'/'+histo_key.replace(' ', '_')

        output_dirname = os.path.dirname(output_basename_woExt)
        if not os.path.isdir(output_dirname): EXE('mkdir -p '+output_dirname)

        for _ext in EXTS:

            out_file = output_basename_woExt+'.'+_ext

            canvas.SaveAs(out_file)

            print '\033[1m'+'\033[92m'+'[output]'+'\033[0m', out_file

        canvas.Close()
    ### -------------------

#!/usr/bin/env python
import argparse
import os
import array
import ROOT

NBINS = 50

SCALE = 500.

VAL0_THRESHOLD = 100.

#### main
if __name__ == '__main__':
   ### args --------------
   parser = argparse.ArgumentParser()

   parser.add_argument('-n', dest='nevents', action='store', default=int(1e5), type=int,
                       help='number of entries')

   parser.add_argument('-m', '--mean', dest='mean', action='store', default=0, type=int,
                       help='mean offset value (unit: percentage)')

   parser.add_argument('-r', '--resolution', dest='resolution', action='store', required=True, type=int,
                       help='resolution value (unit: percentage)')

   parser.add_argument('-s', '--seed', dest='seed', action='store', default=1234, type=int,
                       help='seed for random number generator')

   parser.add_argument('-o', '--output', dest='output', action='store', default=None, required=True,
                       help='path to output .root file')

   parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                       help='enable verbose mode')

   opts, opts_unknown = parser.parse_known_args()
   ### -------------------

   if not (-100 <= opts.mean <= 100):
      raise RuntimeError('invalid mean offset value: '+str(opts.mean))

   if not (0 <= opts.resolution <= 100):
      raise RuntimeError('invalid resolution value: '+str(opts.resolution))

   outkey_postfix = 'offsetN' if opts.mean < 0 else 'offsetP'
   outkey_postfix += '{:03d}'.format(abs(opts.mean))
   outkey_postfix += '_resolution{:03d}'.format(opts.resolution)

   mean = opts.mean/100.
   resolution = opts.resolution/100.

   rand = ROOT.TRandom3()

   rand.SetSeed(opts.seed)

   val0_values = []
   val1_values = []

   for i_evt in range(opts.nevents):

       i_val1 = rand.Rndm() * SCALE
       i_val0 = max(0, (rand.Gaus(mean, resolution) + 1) * i_val1)

       val0_values += [i_val0]
       val1_values += [i_val1]

   binlist = array.array('d', [(_tmp * SCALE / NBINS) for _tmp in range(NBINS+1)])

   hNum = ROOT.TH1F('hNum_'+outkey_postfix, 'hNum_'+outkey_postfix, len(binlist)-1, binlist)
   hDen = ROOT.TH1F('hDen_'+outkey_postfix, 'hDen_'+outkey_postfix, len(binlist)-1, binlist)

   hNum.SetBinErrorOption(ROOT.TH1.kPoisson)
   hDen.SetBinErrorOption(ROOT.TH1.kPoisson)

   for i_evt in range(opts.nevents):

       hDen.Fill(val1_values[i_evt])

       if val0_values[i_evt] > VAL0_THRESHOLD:
          hNum.Fill(val1_values[i_evt])

   geff = ROOT.TGraphAsymmErrors(hNum, hDen, 'cl=0.683 b(1,1) mode')
   geff.SetName('geff_'+outkey_postfix)
   geff.SetTitle(geff.GetName())

   output_tfile = ROOT.TFile(opts.output, 'update')
   if (not output_tfile) or output_tfile.IsZombie() or output_tfile.TestBit(ROOT.TFile.kRecovered): raise SystemExit(1)
   
#   if not output_tfile.Get(hNum.GetName()):
#      print '\033[1m'+'\033[93m'+'[output]'+'\033[0m', hNum.GetName()
#      hNum.Write()
#
#   if not output_tfile.Get(hDen.GetName()):
#      print '\033[1m'+'\033[93m'+'[output]'+'\033[0m', hDen.GetName()
#      hDen.Write()

   if not output_tfile.Get(geff.GetName()):
      print '\033[1m'+'\033[92m'+'[output]'+'\033[0m', geff.GetName()
      geff.Write()

   output_tfile.Close()

#   print '\033[1m'+'\033[92m'+'[output]'+'\033[0m', opts.output

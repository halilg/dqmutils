#!/usr/bin/env python
"""run.py
"""
import argparse
import os

from common import *

#### main
if __name__ == '__main__':
    ### args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-o', '--output', dest='output', action='store', default=None, required=True,
                        help='path to output directory')

    parser.add_argument('-c', '--cfg', dest='cmsRun_cfg_file', action='store', default=os.path.dirname(os.path.abspath(__file__))+'/DQM_cfg.py',
                        help='path to configuration file to be processed by cmsRun')

    parser.add_argument('--cfg-harvesting', dest='cmsRun_cfg_file_harvesting', action='store', default=os.path.dirname(os.path.abspath(__file__))+'/harvesting_cfg.py',
                        help='path to HARVESTING configuration file to be processed by cmsRun')

    parser.add_argument('--no-harvesting', dest='no_harvesting', action='store_true', default=False,
                        help='skip Harvesting step')

    parser.add_argument('-d', '--dry-run', dest='dry_run', action='store_true', default=False,
                        help='enable dry-run mode')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    opts, opts_unknown = parser.parse_known_args()
    ### -------------------------

    log_prx = os.path.basename(__file__)+' -- '

    ### unrecognized command-line arguments
    if opts_unknown:
       KILL(log_prx+'unrecognized command-line arguments: '+str(opts_unknown))

    ### opts --------------------
    VERBOSE = bool(opts.verbose)

    if os.path.exists(opts.output):
       KILL(log_prx+'target path to output directory already exists [-o]: '+str(opts.output))

    OUTPUT_DIR = os.path.abspath(opts.output)

    if not os.path.isfile(opts.cmsRun_cfg_file):
       KILL(log_prx+'invalid path to configuration file to be processed by cmsRun [-c]: '+str(opts.cmsRun_cfg_file))

    CMSRUN_CFG_FILE_DQM = os.path.abspath(opts.cmsRun_cfg_file)
    ### -------------------------

    cmds = [

      'mkdir -p '+OUTPUT_DIR,
      'cd '+OUTPUT_DIR,
      'cp '+CMSRUN_CFG_FILE_DQM+' '+OUTPUT_DIR,
      'cmsRun '+CMSRUN_CFG_FILE_DQM,
    ]

    if not opts.no_harvesting:

       CMSRUN_CFG_FILE_HAR = os.path.abspath(opts.cmsRun_cfg_file_harvesting)

       if not os.path.isfile(CMSRUN_CFG_FILE_HAR):
          KILL(log_prx+'invalid path to configuration file to be processed by cmsRun (step: Harvesting): '+str(CMSRUN_CFG_FILE_HAR))

       cmds += [

         'cp '+CMSRUN_CFG_FILE_HAR+' '+OUTPUT_DIR,
         'cmsRun '+CMSRUN_CFG_FILE_HAR,
       ]

    EXE(' && '.join(cmds), verbose=opts.verbose, dry_run=opts.dry_run)

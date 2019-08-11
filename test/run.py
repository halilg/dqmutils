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
    ### -------------------------

    cmds = [

      'mkdir -p '+OUTPUT_DIR,
      'cd '+OUTPUT_DIR,
      'cmsRun '+os.path.dirname(os.path.abspath(__file__))+'/DQM_cfg.py',
    ]

    if not opts.no_harvesting:
       cmds += ['cmsRun '+os.path.dirname(os.path.abspath(__file__))+'/harvesting_cfg.py']

    EXE(' && '.join(cmds), verbose=opts.verbose, dry_run=opts.dry_run)

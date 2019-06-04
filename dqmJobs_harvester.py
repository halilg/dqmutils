#!/usr/bin/env python
"""dqmJobs_harvester.py
"""
import argparse
import os
import math

from common import *

def cmsDriver_command(workflow):

    res ="""cmsDriver.py stepHarvesting \\
 --step HARVESTING:hltOfflineDQMClient --harvesting AtRunEnd \\
 --filein filelist:inputs.txt \\
 --python_filename harvesting_cfg.py \\
 --filetype DQM \\
 --mc \\
 --scenario pp \\
 --conditions auto:phase1_2018_realistic \\
 --era Run2_2018 \\
 --geometry DB:Extended \\
 --no_exec \\
 -n -1 || exit $? ;
"""
    return res

#### main
if __name__ == '__main__':
    ### args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--inputs', dest='inputs', nargs='+', default=[], required=True,
                        help='path to input file(s) [format: DQM]')

    parser.add_argument('-o', '--output', dest='output', action='store', default=None, required=True,
                        help='path to output directory')

#    parser.add_argument('--name', dest='name', action='store', default='dqmjob', required=False,
#                        help='prefix of output files\' names (example: [NAME]_[counter].[ext])')

    parser.add_argument('-l', '--list-workflow', dest='list_workflow', nargs='+', default=[], required=True,
                        help='list of workflows (each corresponds to cmsDriver.py directive for Harvesting)')

#    parser.add_argument('-n', '--n-events', dest='n_events', action='store', type=int, default=-1, required=False,
#                        help='maximum number of events per job (used as argument of "-n" option in cmsDriver.py)')

    parser.add_argument('--max-inputs', dest='max_inputs', action='store', type=int, default=-1, required=False,
                        help='maximum number of input files to be processed (if integer is negative, all files will be processed)')

#    parser.add_argument('--exe-format-input', dest='exe_format_input', action='store', default='root',
#                        help='format of input file to be used by executable via "-i" (name of file extension without dot)')

#    parser.add_argument('--exe-format-output', dest='exe_format_output', action='store', default='root',
#                        help='format of output file to be used by executable via "-o" (name of file extension without dot)')

#    parser.add_argument('--output-postfix', dest='output_postfix', action='store', default=None,
#                        help='post-fix to output basename (example: seed number when generating toys)')

    parser.add_argument('--skipBadFiles', dest='skipBadFiles', action='store_true', default=False,
                        help='skip invalid inputs without stopping execution (enables option skipBadFiles in PoolSource)')

    parser.add_argument('--no-exec', dest='no_exec', action='store_true', default=False,
                        help='do not run cmsRun on harvesting cfg file')

    parser.add_argument('--permissive', dest='permissive', action='store_true', default=False,
                        help='do not stop execution because of warnings (messages will still be sent to stdout)')

#    parser.add_argument('--permissive', dest='permissive', action='store_true', default=False,
#                        help='do not stop execution because of warnings (messages will still be sent to stdout)')

    parser.add_argument('--dry-run', dest='dry_run', action='store_true', default=False,
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

#    if not os.path.isdir(opts.input):
#       KILL(log_prx+'target path to input directory is not valid [-i]: '+str(opts.input))

    if os.path.exists(opts.output):
       KILL(log_prx+'target path to output directory already exists [-o]: '+str(opts.output))

#    if opts.n_events == 0:
#       KILL(log_prx+'logic error: requesting zero events per job (use non-zero value for argument of option "-n")')

#    INPUT_DIR  = os.path.abspath(opts.input)
    OUTPUT_DIR = os.path.abspath(opts.output)
    ### -------------------------

    ### create list of relative paths to input files
    INPUT_FILES = []
    for i_inputf in opts.inputs:

        if i_inputf.startswith('file:'):
           if not os.path.isfile(i_inputf[len('file:'):]):
              KILL(log_prx+'invalid path to target local file: '+i_inputf)

           i_inputf = 'file:'+os.path.abspath(i_inputf[len('file:'):])

        elif os.path.isfile(i_inputf):
           i_inputf = 'file:'+os.path.abspath(i_inputf)

        elif not i_inputf.startswith('/store/'):
           KILL(log_prx+'invalid path to target remote file (path does not start with "/store/"): '+i_inputf)

        INPUT_FILES += [i_inputf]

    INPUT_FILES = sorted(list(set(INPUT_FILES)))

    EXE('mkdir '+OUTPUT_DIR)

    file_inputs_path = OUTPUT_DIR+'/inputs.txt'
    file_inputs = open(file_inputs_path, 'w')
    for _tmp in INPUT_FILES: file_inputs.write(_tmp+'\n')
    file_inputs.close()

    file_Harvesting_setup_path = OUTPUT_DIR+'/harvesting_setup.sh'
    file_Harvesting_setup = open(file_Harvesting_setup_path, 'w')

    file_Harvesting_setup.write('#!/bin/bash'+'\n\n')

    Harvesting_setup_cmd = cmsDriver_command(opts.list_workflow)
    file_Harvesting_setup.write(Harvesting_setup_cmd)

    if not opts.no_exec:
       file_Harvesting_setup.write('\n'+'cmsRun harvesting_cfg.py'+'\n')

    file_Harvesting_setup.close()

    EXE('chmod u+x '+file_Harvesting_setup_path)

    EXE('cd '+OUTPUT_DIR+' && '+file_Harvesting_setup_path)

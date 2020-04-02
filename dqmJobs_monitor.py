#!/usr/bin/env python
"""dqmJobs_monitor.py: script to monitor batch jobs
  * finds all batch scripts, e.g. "XXX.htc" for HTCondor and "XXX.sh" for SGE, in the input directory (including sub-directories)
  * if a file called "XXX.completed" exists, the job is considered finished
  * otherwise, the job is resubmitted if option "-r" is specified
"""

import argparse
import os
import math
import ROOT

from common import *

#### main
if __name__ == '__main__':
    ### args
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-i', '--inputs', dest='inputs', nargs='+', default=[], required=True,
                        help='list of paths to input directories')

    parser.add_argument('--batch', dest='batch', choices=['htc', 'sge'], action='store', default='htc',
                        help='type of batch system for job submission (default: HTCondor)')

    parser.add_argument('--skip', dest='skip', nargs='+', default=[],
                        help='list of job-ID numbers to be ignored')

    parser.add_argument('-r', '--resubmit', dest='resubmit', action='store_true', default=False,
                        help='enable resubmission of batch jobs')

    parser.add_argument('--check-root', dest='check_root', action='store_true', default=False,
                        help='check integrity of ROOT output before marking job as completed')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    parser.add_argument('-d', '--dry-run', dest='dry_run', action='store_true', default=False,
                        help='enable dry-run mode')

    opts, opts_unknown = parser.parse_known_args()
    ###

    ROOT.gROOT.SetBatch()

    log_prx = os.path.basename(__file__)+' -- '

    if opts_unknown:
       KILL(log_prx+'unsupported command-line arguments: '+str(opts_unknown))

    # input directories
    INPUT_DIRS = []

    for i_opt in opts.inputs:

        if not os.path.isdir(i_opt):
           WARNING(log_prx+'input argument is not a valid directory: '+i_opt)

        INPUT_DIRS += [i_opt]

    INPUT_DIRS = list(set(INPUT_DIRS))

    # batch system
    BATCH_HTC = bool(opts.batch == 'htc')

    if BATCH_HTC: which('condor_q')
    else        : which('qstat')

    EXT_INP = 'htc' if BATCH_HTC else 'sh'
    EXT_OUT = 'completed'

    if EXT_INP == EXT_OUT:
       KILL(log_prx+'logic error: extensions of input and output files are identical')

    counter_input     = 0
    counter_resub     = 0
    counter_runng     = 0
    counter_completed = 0

    FILES_INPUT     = []
    FILES_COMPLETED = []

    for input_dir in INPUT_DIRS:

        for path, subdirs, files in os.walk(input_dir, followlinks=True):

            for name in files:

                if name.endswith(EXT_INP):

                   i_finp = os.path.join(path, name)

                   FILES_INPUT += [i_finp]

                   i_fout = os.path.splitext(i_finp)[0]+'.'+EXT_OUT

                   if os.path.isfile(i_fout):
                      FILES_COMPLETED += [os.path.abspath(i_fout)]

    counter_input     = len(FILES_INPUT)
    counter_completed = len(FILES_COMPLETED)

    if counter_input < counter_completed:
       KILL(log_prx+'logic error: found more output files ('+str(counter_completed)+') than input files ('+str(counter_input)+')')

    elif (counter_input > counter_completed) or opts.check_root:

      counter_completed = 0

      #
      # find script(s) running (or stuck) on batch system
      #
      # * current implementation:
      #   - if stuck, don't resubmit (clean by hand, then rerun runFolder.py)
      #
      RUNNG_FILES = []

      if BATCH_HTC:

         if opts.skip:

            running_jobIDs = HTCondor_jobIDs(os.environ['USER'])

            for i_runn_jobID in running_jobIDs:

                if i_runn_jobID in opts.skip: continue

                i_runn_exepath = HTCondor_executable_from_jobID(i_runn_jobID)

                if i_runn_exepath != None:

                   i_runn_htcpath = os.path.splitext(i_runn_exepath)[0]+'.'+EXT_INP

                   RUNNG_FILES += [os.path.abspath(os.path.realpath(i_runn_htcpath))]

         else:

            running_jobExes = HTCondor_jobExecutables(os.environ['USER'])

            for i_runn_exepath in running_jobExes:

                i_runn_htcpath = os.path.splitext(i_runn_exepath)[0]+'.'+EXT_INP

                RUNNG_FILES += [os.path.abspath(os.path.realpath(i_runn_htcpath))]

      else:

         qstat_lines = get_output('qstat')[0].split('\n')
         qstat_lines = [_tmp for _tmp in qstat_lines if _tmp != '']

         if len(qstat_lines) > 2: qstat_lines = qstat_lines[2:]

         for qstat_l in qstat_lines:

             qstat_jobN = qstat_l.split()[0]

             if qstat_jobN in opts.skip: continue

             qstat_j = get_output('qstat -j '+qstat_jobN+' | grep script_file', permissive=True)[0].split('\n')
             qstat_j = [_tmp for _tmp in qstat_j if _tmp != '']

             if len(qstat_j) != 1: continue

             qstat_j_pieces = qstat_j[0].split()
             if len(qstat_j_pieces) != 2: continue

             qstat_script = os.path.abspath(os.path.realpath(qstat_j_pieces[1]))

             RUNNG_FILES += [qstat_script]
      # ---

      FILES_INPUT_NotRunning = []
      for input_file in FILES_INPUT:

          f_runng = bool(os.path.abspath(os.path.realpath(input_file)) in RUNNG_FILES)

          if f_runng: counter_runng += 1
          else      : FILES_INPUT_NotRunning += [input_file]

      FILES_RESUB = []

      for input_file in FILES_INPUT_NotRunning:
          input_file_woEXT = os.path.splitext(input_file)[0]

          output_file = input_file_woEXT+'.'+EXT_OUT

          if os.path.exists(output_file):

             if opts.check_root:

                output_file_root = input_file_woEXT+'.root'

                if os.path.isfile(output_file_root):

                   output_tfile_root = ROOT.TFile.Open(output_file_root)

                   if (not output_tfile_root) or output_tfile_root.IsZombie() or output_tfile_root.TestBit(ROOT.TFile.kRecovered):

                      FILES_RESUB += [input_file]

                      output_tfile_root.Close()

                      continue

                   output_tfile_root.Close()

                   if opts.verbose: print 'output ROOT file is valid:', output_file_root

             counter_completed += 1

          else:
             FILES_RESUB += [input_file]

      counter_resub += len(FILES_RESUB)

      FILES_RESUB.sort()

      for resub_file in FILES_RESUB:

          if opts.resubmit:

             print colored_text('> resubmitting job:', ['93']), colored_text(resub_file, ['1', '93'])

             resub_file_abspath = os.path.abspath(os.path.realpath(resub_file))

             resub_cmd = 'condor_submit' if BATCH_HTC else 'qsub'

             EXE(resub_cmd+' '+resub_file_abspath, verbose=opts.verbose, dry_run=opts.dry_run)

          else:

             print colored_text('> job to be resubmitted:', ['93']), colored_text(resub_file, ['1', '93'])

    counter_format = '{:>'+str(1+int(math.log10(counter_input)))+'}' if counter_input > 0 else '{:>1}'

    print ''
    print '-'*51
    print ''
    print ' Number of input  files found : '+colored_text(counter_format.format(counter_input)    , ['1',     ])
    print ' Number of output files found : '+colored_text(counter_format.format(counter_completed), ['1', '92'])

    if opts.resubmit: print ' Number of resubmitted jobs   : '+colored_text(counter_format.format(counter_resub), ['1', '93'])
    else            : print ' Number of jobs to resubmit   : '+colored_text(counter_format.format(counter_resub), ['1', '93'])

    print ''
    print ' Number of jobs still running : '+counter_format.format(counter_runng)
    print ''
    print '-'*51
    print ''

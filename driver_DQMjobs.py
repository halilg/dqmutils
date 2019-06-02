#!/usr/bin/env python
"""driver.py -- creates scripts for batch-submission of DQM jobs
"""
import argparse
import os
import math

from common import *

def batch_job_HTCondor(**kwargs):

    _OUTPUT_DIR = os.path.abspath(os.path.realpath(kwargs['output_directory']))

    EXE('mkdir -p '+_OUTPUT_DIR+'/'+kwargs['output_subdirectory'], verbose=kwargs['verbose'], dry_run=kwargs['dry_run'])

    _OFILE_ABSPATH = _OUTPUT_DIR+'/'+kwargs['output_basename']+'.sh'

    if os.path.exists(_OFILE_ABSPATH):
       KILL(log_prx+' -- batch_job_HTCondor: target output file already exists: '+_OFILE_ABSPATH)

    # batch configuration options
    _OPTS = [
      'batch_name = '+kwargs['output_basename'],

      'executable = '+_OFILE_ABSPATH,

      'output = '+_OUTPUT_DIR+'/'+kwargs['output_subdirectory']+'/'+kwargs['output_basename']+'.out.$(Cluster).$(Process)',
      'error  = '+_OUTPUT_DIR+'/'+kwargs['output_subdirectory']+'/'+kwargs['output_basename']+'.err.$(Cluster).$(Process)',
      'log    = '+_OUTPUT_DIR+'/'+kwargs['output_subdirectory']+'/'+kwargs['output_basename']+'.log.$(Cluster).$(Process)',

      '#arguments = ',

      'transfer_executable = True',

      'universe = vanilla',

      'getenv = True',

      'should_transfer_files   = IF_NEEDED',
      'when_to_transfer_output = ON_EXIT',

      'requirements = (OpSysAndVer == "SL6")',
      '#requirements = (OpSysAndVer == "SL6" || OpSysAndVer == "CentOS7")',

      ' RequestMemory  =  2000',
      '+RequestRuntime = 10800',

      'queue',
    ]

    _UPDATED_OPTS = []

    _ADDED_OPTS = (kwargs['submit_options'] if 'submit_options' in kwargs else [])

    for _tmp_opt in _OPTS[:-1]:

        _tmp_opt_keyw = _tmp_opt.split('=')[0].replace(' ','')

        _tmp_skip_opt = False

        for _tmp_add_opt in _ADDED_OPTS:

            _tmp_add_opt_keyw = _tmp_add_opt.split('=')[0].replace(' ','')

            if _tmp_opt_keyw == _tmp_add_opt_keyw: _tmp_skip_opt = True; break;

        if _tmp_skip_opt: continue

        _UPDATED_OPTS += [_tmp_opt]

    for _tmp_add_opt in _ADDED_OPTS: _UPDATED_OPTS += [_tmp_add_opt]

    if 'queue' not in _UPDATED_OPTS[-1]: _UPDATED_OPTS += ['queue']

    _o_file = open(_OFILE_ABSPATH, 'w')

    _o_shebang = '#!/bin/bash'
    _o_file.write(_o_shebang+'\n')

    # HTCondor getenv=True does not export LD_LIBRARY_PATH
    # --> added by hand in the script itself
    if 'LD_LIBRARY_PATH' in os.environ:
       _o_file.write('\n'+'export LD_LIBRARY_PATH='+os.environ['LD_LIBRARY_PATH']+'\n')

    _o_file.write('\n'+kwargs['output_string']+'\n')

    _o_file.close()

    print '\033[1m'+'\033[94m'+'output:'+'\033[0m', os.path.relpath(_OFILE_ABSPATH, os.environ['PWD'])

    EXE('chmod u+x '+_OFILE_ABSPATH, verbose=kwargs['verbose'], dry_run=kwargs['dry_run'])

    _OFCFG_ABSPATH = os.path.splitext(_OFILE_ABSPATH)[0]+'.htc'

    _o_fcfg = open(_OFCFG_ABSPATH, 'w')

    for _tmp in _UPDATED_OPTS: _o_fcfg.write(_tmp+'\n')

    _o_fcfg.close()

    if kwargs['submit']:
       EXE('condor_submit '+_OFCFG_ABSPATH, suspend=False, verbose=kwargs['verbose'], dry_run=kwargs['dry_run'])

    return

def convert_args_to_lines(args):

    _tmp_lines = []

    _tmp_idxs = [0] + [i_idx for i_idx, i_opt in enumerate(args) if i_opt.startswith('-') and not (is_int(i_opt) or is_float(i_opt))] + [len(args)]
    _tmp_idxs = sorted(list(set(_tmp_idxs)))

    for j_idx in range(len(_tmp_idxs)-1):
        _tmp_lines += [' '.join(args[_tmp_idxs[j_idx]:_tmp_idxs[j_idx+1]])]

    del _tmp_idxs

    return _tmp_lines

#### main
if __name__ == '__main__':
    ### args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

#    parser.add_argument('-i', '--input', dest='input', action='store', default=None, required=True,
#                        help='path to input directory')

    parser.add_argument('-d', '--das-dataset', dest='das_dataset', action='store', default=None, required=True,
                        help='name of input dataset in DAS')

    parser.add_argument('-o', '--output', dest='output', action='store', default=None, required=True,
                        help='path to output directory')

    parser.add_argument('--name', dest='name', action='store', default='dqmjob', required=False,
                        help='prefix of output files\' names (example: [NAME]_[counter].[ext])')

    parser.add_argument('-s', '--step', dest='step', action='store', default=None, required=True,
                        help='argument of option "--step" of cmsDriver.py')

    parser.add_argument('-e', '--era', dest='era', action='store', default=None, required=True, choices=['2016', '2017', '2018'],
                        help='path to executable file used in batch job(s)')

    parser.add_argument('-n', '--n-events', dest='n_events', action='store', type=int, default=-1, required=False,
                        help='maximum number of events per job (used as argument of "-n" option in cmsDriver.py)')

    parser.add_argument('--max-inputs', dest='max_inputs', action='store', type=int, default=-1, required=False,
                        help='maximum number of input files to be processed (if integer is negative, all files will be processed)')

#    parser.add_argument('--exe-format-input', dest='exe_format_input', action='store', default='root',
#                        help='format of input file to be used by executable via "-i" (name of file extension without dot)')

#    parser.add_argument('--exe-format-output', dest='exe_format_output', action='store', default='root',
#                        help='format of output file to be used by executable via "-o" (name of file extension without dot)')

#    parser.add_argument('--output-postfix', dest='output_postfix', action='store', default=None,
#                        help='post-fix to output basename (example: seed number when generating toys)')

    parser.add_argument('--batch', dest='batch', choices=['htc'], action='store', default='htc',
                        help='type of batch system for job submission')

    parser.add_argument('--htc-opts', dest='htc_opts', nargs='+', default=[],
                        help='list of options for HTCondor submission script')

    parser.add_argument('--submit', dest='submit', action='store_true', default=False,
                        help='submit job(s) on the batch system')

    parser.add_argument('--dry-run', dest='dry_run', action='store_true', default=False,
                        help='enable dry-run mode')

    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help='enable verbose mode')

    opts, opts_unknown = parser.parse_known_args()
    ### -------------------------

    log_prx = os.path.basename(__file__)+' -- '

    ### opts --------------------
    VERBOSE = bool(opts.verbose and (not opts.submit))

#    if not os.path.isdir(opts.input):
#       KILL(log_prx+'target path to input directory is not valid [-i]: '+str(opts.input))

    if os.path.exists(opts.output):
       KILL(log_prx+'target path to output directory already exists [-o]: '+str(opts.output))

#    if not os.path.isfile(opts.executable):
#       KILL(log_prx+'target path to executable file used in batch job(s) [-e]: '+str(opts.executable))

    if opts.n_events == 0:
       KILL(log_prx+'logic error: requesting zero events per job (use non-zero value for argument of option "-n")')

    if opts.batch != None:
       if opts.submit and (not opts.dry_run):
          if opts.batch == 'htc': which('condor_submit')

#    INPUT_DIR  = os.path.abspath(opts.input)
    OUTPUT_DIR = os.path.abspath(opts.output)

#    EXEC_FILE_ABSPATH = os.path.abspath(opts.executable)

    ### unrecognized command-line arguments
    if opts_unknown:
       KILL(log_prx+'unrecognized command-line arguments: '+str(opts_unknown))
    ### -------------------------

    ### create list of relative paths to input files
    das_dataset_files = command_output_lines('dasgoclient --query "file dataset='+str(opts.das_dataset)+'"')
    das_dataset_files = [_tmp for _tmp in das_dataset_files if _tmp != '']
    das_dataset_files = sorted(list(set(das_dataset_files)))

    if len(das_dataset_files) == 0:
       KILL(log_prx+'empty list of input files for dataset: '+str(opts.das_dataset))

    if opts.max_inputs == 0:
       KILL(log_prx+'logic error: requesting a maximum of zero input files (use non-zero value for argument of option --max-inputs)')

    elif opts.max_inputs > 0:
       das_dataset_files = das_dataset_files[:opts.max_inputs]

    outputname_postfix_format = '_{:0'+str(1+int(math.log10(len(das_dataset_files))))+'d}'

    ### create output script(s)
    for i_inputfile_idx, i_inputfile in enumerate(das_dataset_files):

        # executable's input file
        i_INPUT_FILE = i_inputfile

        # basename of output file without file extension
        i_OUTPUT_BASENAME_woExt = opts.name+outputname_postfix_format.format(i_inputfile_idx+1)

        # name of output sub-directory
        i_OUTPUT_DIR = OUTPUT_DIR+'/'+i_OUTPUT_BASENAME_woExt

        i_SHELL_COMMANDS  = [['set -e']]

        i_SHELL_COMMANDS += [['cd '+i_OUTPUT_DIR]]

        i_SHELL_COMMANDS += [['INPUT_EDM_FILE='+i_inputfile]]

        i_SHELL_COMMANDS += [['OUTPUT_TAG='+i_OUTPUT_BASENAME_woExt]]

        if   opts.era =='2016': i_SHELL_COMMANDS += [['OPT_CONDITIONS=auto:phase1_2016_realistic'], ['OPT_ERA=Run2_2016'],]
        elif opts.era =='2017': i_SHELL_COMMANDS += [['OPT_CONDITIONS=auto:phase1_2017_realistic'], ['OPT_ERA=Run2_2017'],]
        elif opts.era =='2018': i_SHELL_COMMANDS += [['OPT_CONDITIONS=auto:phase1_2018_realistic'], ['OPT_ERA=Run2_2018'],]
        else:
          KILL(log_prx+'invalid argument for option "--era": '+str(opts.era))

        i_SHELL_COMMANDS += [['N_EVENTS='+str(opts.n_events)]]

        i_SHELL_COMMANDS += [['STEP1_STEP='+str(opts.step)]]

        i_SHELL_COMMANDS += [["""\
STEP1_OUTPUT=${OUTPUT_TAG}_DQM.root
STEP1_CFG_PY=${OUTPUT_TAG}_DQM_cfg.py
STEP2_CFG_PY=${OUTPUT_TAG}_Harvesting_cfg.py

# --- Step_1: DQM
if [ ! -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step1 \\
   --step ${STEP1_STEP} \\
   --filein          ${INPUT_EDM_FILE} \\
   --fileout         ${STEP1_OUTPUT} \\
   --python_filename ${STEP1_CFG_PY} \\
   --mc \\
   --eventcontent DQM \\
   --datatier DQMIO \\
   --conditions ${OPT_CONDITIONS} \\
   --era ${OPT_ERA} \\
   --geometry DB:Extended \\
   --nThreads 1 \\
   --no_exec \\
   --runUnscheduled \\
   --customise Configuration/DataProcessing/Utils.addMonitoring \\
   -n ${N_EVENTS} || exit $? ;

  cmsRun ${STEP1_CFG_PY}

else

  printf "\\n%s\\n\\n" " >>> WARNING -- skipped Step_1 , target output file already exists: ${STEP1_OUTPUT}"
fi

# --- Step_2: Harvesting (output: DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root)

if [ -f ${STEP1_OUTPUT} ]; then

  cmsDriver.py step2 \\
   --step HARVESTING:hltOfflineDQMClient --harvesting AtRunEnd \\
   --filein     file:${STEP1_OUTPUT} \\
   --python_filename ${STEP2_CFG_PY} \\
   --filetype DQM \\
   --mc \\
   --scenario pp \\
   --conditions ${OPT_CONDITIONS} \\
   --era ${OPT_ERA} \\
   --geometry DB:Extended \\
   --no_exec \\
   -n ${N_EVENTS} || exit $? ;

  cmsRun ${STEP2_CFG_PY}

else

  printf "\\n%s\\n\\n" " >>> WARNING -- skipped Step_2 , target input file not found: ${STEP1_OUTPUT}"
fi\
"""
        ]]

        i_SHELL_COMMANDS += [['touch '+i_OUTPUT_BASENAME_woExt+'.completed']]

        if opts.batch == 'htc':

           batch_job_HTCondor(**{

             'output_string': '\n\n'.join([' \\\n '.join(_tmp) for _tmp in i_SHELL_COMMANDS]),

             'output_basename': i_OUTPUT_BASENAME_woExt,

             'output_directory': i_OUTPUT_DIR,

             'output_subdirectory': opts.batch,

             'submit' : opts.submit,

             'submit_options': opts.htc_opts,

             'verbose': VERBOSE,

             'dry_run': opts.dry_run,
           })

        else:
           KILL(log_prx+'unsupported type of batch submission system: '+str(opts.batch))

    ## ----------------

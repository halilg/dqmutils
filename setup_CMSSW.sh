#!/bin/sh

if   [ $(basename ${SHELL}) = "bash" ]; then BASE_DIR=$(dirname $(readlink -f ${BASH_SOURCE}))
elif [ $(basename ${SHELL}) = "zsh"  ]; then BASE_DIR=$(dirname $(readlink -f $0))
else

  printf "\n%s\n\n" " >>> WARNING -- unsupported type of shell: ${SHELL}"
  return
fi

if [ ! -f ${BASE_DIR}/setup_CMSSW.sh ]; then

  printf "\n%s\n\n" " >>> ERROR -- invalid path to directory containing setup_CMSSW.sh script: \"${BASE_DIR}\""
  unset -v BASE_DIR
  return
fi

cd ${BASE_DIR}
unset -v BASE_DIR

CMSSW_rel=CMSSW_10_6_0_pre2

if [ ! -d ${CMSSW_rel} ]; then
  cmsrel  ${CMSSW_rel}
fi

cd ${CMSSW_rel}/src
unset -v CMSSW_rel

# cmsenv
eval `scram runtime -sh`

# voms
voms-proxy-init --voms cms

# DQM step
if [ ! -d DQMOffline/Trigger ]; then git cms-addpkg DQMOffline/Trigger; fi;

# Validation step
if [ ! -d HLTriggerOffline ]; then git cms-addpkg HLTriggerOffline; fi;

scram b
scram b

cd ${CMSSW_BASE}/..

#!/bin/bash

# dasgoclient --query="file dataset=/MuonEG/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD run=323755"

mkdir -p nanoAOD_323755_MuonEG
cd       nanoAOD_323755_MuonEG

xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/MuonEG/NANOAOD/Nano14Dec2018_ver2-v1/40000/CAA0849F-8EBC-7245-AB28-2C9956E08DD5.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/MuonEG/NANOAOD/Nano14Dec2018_ver2-v1/40000/E64CB33B-3DB8-8846-9127-A11B86C8BEB3.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/MuonEG/NANOAOD/Nano14Dec2018_ver2-v1/40000/F4B1CE43-FB97-064C-9177-757A96835AA3.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/MuonEG/NANOAOD/Nano14Dec2018_ver2-v1/40000/BA5FA145-F861-5C47-9527-EE8DCC07D494.root .

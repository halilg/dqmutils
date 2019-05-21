#!/bin/bash

# dasgoclient --query="file dataset=/DoubleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD run=323755"

mkdir -p nanoAOD_323755_DoubleMuon
cd       nanoAOD_323755_DoubleMuon

xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/4A1F98FE-796B-514A-A5D9-727DF6E91246.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/83529470-E992-4245-82B8-5DEC44C8D23E.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/5E8BB35F-01A5-E744-8D22-BB3CBCD7A589.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/31136911-8BF6-3947-8A35-5BD836AB7326.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/14DFC2DB-E0B6-AE4F-9F4A-4F948FBA7CD8.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/78A5E018-06A6-F148-A7D2-DEEC9893EE55.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/A9229257-9437-2344-AECB-70699AA1B5E7.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/10000/8B40A31B-130E-9747-9B06-C41503A69A7D.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/0F06AE38-EAB6-284C-AA21-86C1A92E77FF.root .

#!/bin/bash

# dasgoclient --query="file dataset=/SingleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD run=323755"

mkdir -p nanoAOD_323755_SingleMuon
cd       nanoAOD_323755_SingleMuon

xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/13989512-4B0A-AF40-9465-981805563B71.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/DA64DF75-5AD6-1E4B-BA93-BC52E8EA14FF.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/40000/B88E7072-4415-8B47-92BC-5ED1A8FE2850.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/C98EB94E-95E9-2141-8AE9-B8A890FAE3CA.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/83BAB8E0-F683-C140-A1D5-B8C4FEB85835.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/363573E5-F391-F447-8B33-AF7C69ADCFE7.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/C3AAAB72-8FCF-5145-820C-04C7045AB343.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/C60F24BC-2D58-F247-978C-0F15827D4C8D.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/SingleMuon/NANOAOD/Nano14Dec2018_ver2-v1/00000/BA01EB81-E666-1A4C-9907-A9A76B621D19.root .

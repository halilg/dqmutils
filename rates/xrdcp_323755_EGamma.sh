#!/bin/bash

# dasgoclient --query="file dataset=/EGamma/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD run=323755"

mkdir -p nanoAOD_323755_EGamma
cd       nanoAOD_323755_EGamma

xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/4825D146-4298-2A43-AA14-4230EDC5343D.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/5EA087D0-2C26-0649-A7F6-EBC676E32F81.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E5496B7C-05F0-CD46-AF48-EAF143DC415C.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/DDE966F5-6F11-3249-8B6B-D4AB4ED1BD14.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/B9CA6D8F-D063-DF4A-95B8-6B935FF8AA93.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/328DD0A7-8D2E-D741-8F11-829C08A8A9C4.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D7D68BA4-5939-9F40-8113-79C3A4E67D51.root .
xrdcp root://cmsxrootd.fnal.gov//store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/836F152C-86B7-0746-817C-CF8E567278AF.root .

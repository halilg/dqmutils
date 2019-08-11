  LogDebug("HLTDQMTester") << "------------------------------------------------------------";

  const bool debug_ = true;

  bool changed(true);

  if(not hltConfig_.init(iRun, iSetup, "HLT", changed)){

    LogDebug("HLTDQMTester") << "HLTConfigProvider failed to initialize.";
  }

  std::string pathname("");
  std::string filtername("");

  const unsigned int numberOfPaths(hltConfig_.size());

  for (unsigned int i = 0; i != numberOfPaths; ++i) {

    bool numFound = false;
    pathname = hltConfig_.triggerName(i);

    unsigned int usedPrescale = 1;
    unsigned int objectType = 0;

    if(debug_){

      std::cout << " - Startup:Path, PS = " << pathname << " , PS = " << hltConfig_.prescaleSize() << std::endl;
    }

    std::vector<std::string> numpathmodules = hltConfig_.moduleLabels(pathname);

    for (auto numpathmodule = numpathmodules.begin(); numpathmodule != numpathmodules.end(); ++numpathmodule) {

      edm::InputTag testTag(*numpathmodule, "", "HLT");

      filtername = *numpathmodule;

      if(debug_){

        std::cout << " - Startup:Module = " << hltConfig_.moduleType(*numpathmodule) << ", FilterName = " << filtername << std::endl;
      }
    }

    if(debug_){

      std::cout << " - Startup:Final filter = " << filtername << std::endl;
    }

////    if(objectType == 0 || numFound == false){ continue; }                                                                                                                                                       

    if(debug_){

      std::cout << "Pathname = " << pathname <<", Filtername = " << filtername << ", ObjectType = " << objectType << std::endl;
    }

//!!    hltPathsAll_.push_back(PathInfo(usedPrescale, pathname, filtername, "HLT", objectType, triggerType));                                                                                                       
  }

#!/bin/bash

tmpcp(){

  echo $@

  local outdir=output_plots_UL16_v06_slim
  local tmpcpa=$(dirname $1)
  mkdir -p ${outdir}/${tmpcpa}

  if [ -f $1 ]; then
    echo $1
    cp $1 ${outdir}/$1
  else
    echo ">> NOT FOUND: "$1
  fi
}

for dd in output_plots_UL16_v06/hltul16_postVFP_vs_80X/TTbar output_plots_UL16_v06/hltul16_postVFP_vs_preVFP/TTbar ; do

  for nnn in 40 80 140; do

    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_All_pt.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_All_eta.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_All_phi.pdf

    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HB_pt.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HB_eta.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HB_phi.pdf

    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HE_pt.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HE_eta.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HE_phi.pdf

    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HF_pt.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HF_eta.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_genjet_HF_phi.pdf

    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_pfjetpT_pTThresh.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_pfjetpT_HB_pTThresh.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_pfjetpT_HE_pTThresh.pdf
    tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK4/PF/HLT_PFJet${nnn}/effic_pfjetpT_HF_pTThresh.pdf

  done
  unset -v nnn

  tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK8/PF/HLT_AK8PFJet80/effic_pfjetpT_pTThresh.pdf
  tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK8/PF/HLT_AK8PFJet80/effic_pfjetpT_HB_pTThresh.pdf
  tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK8/PF/HLT_AK8PFJet80/effic_pfjetpT_HE_pTThresh.pdf
  tmpcp ${dd}/HLT/Run_summary/JME/Jets/AK8/PF/HLT_AK8PFJet80/effic_pfjetpT_HF_pTThresh.pdf

  tmpcp ${dd}/HLT/Run_summary/JME/HT/PFHT250/effic_ht_variable.pdf
  tmpcp ${dd}/HLT/Run_summary/JME/MET/PFMET110/effic_met_variable.pdf
  tmpcp ${dd}/HLT/Run_summary/JME/MET/PFMETNoMu120/effic_met_variable.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/JetHT/effic_JetHT_HLT_PFJet60_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/JetHT/effic_JetHT_HLT_PFJet200_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/JetHT/effic_JetHT_HLT_AK8PFJet200_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/JetHT/effic_JetHT_HLT_PFHT450_SixJet40_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/MET/effic_MET_HLT_PFMET300_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/MET/effic_MET_HLT_PFMET110_PFMHT110_IDTight_v*.pdf
  tmpcp ${dd}/HLT/Run_summary/Filters/MET/effic_MET_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*.pdf

done
unset -v dd

unset -f tmpcp

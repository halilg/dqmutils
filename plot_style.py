#!/usr/bin/env python
import ROOT

def load_plot_style():

    s = ROOT.TStyle('swag', 'plot swagger')

    # For the canvas:
    s.SetCanvasBorderMode(0)
    s.SetCanvasColor(ROOT.kWhite)
    s.SetCanvasDefH(725) #Height of canvas
    s.SetCanvasDefW(800) #Width of canvas
    s.SetCanvasDefX(0)   #POsition on screen
    s.SetCanvasDefY(0)

    # For the Pad:
    s.SetPadBorderMode(0)
    # s.SetPadBorderSize(1)
    s.SetPadColor(ROOT.kWhite)
    s.SetPadGridX(False)
    s.SetPadGridY(False)
    s.SetGridColor(0)
    s.SetGridStyle(3)
    s.SetGridWidth(1)

    # For the frame:
    s.SetFrameBorderMode(0)
    s.SetFrameBorderSize(1)
    s.SetFrameFillColor(0)
    s.SetFrameFillStyle(0)
    s.SetFrameLineColor(1)
    s.SetFrameLineStyle(1)
    s.SetFrameLineWidth(1)

    # For the histo:
    # s.SetHistFillColor(1)
    # s.SetHistFillStyle(0)
    s.SetHistLineColor(4)
    s.SetHistLineStyle(0)
    s.SetHistLineWidth(1)
    # s.SetLegoInnerR(0.5)
    # s.SetNumberContours(20)

    s.SetEndErrorSize(2)
    # s.SetErrorMarker(20)
    #s.SetErrorX(0.)
    
    s.SetMarkerStyle(20)
    
    #For the fit/function:
    s.SetOptFit(1)
    s.SetFitFormat('5.4g')
    s.SetFuncColor(2)
    s.SetFuncStyle(1)
    s.SetFuncWidth(1)

    #For the date:
    s.SetOptDate(0)
    # s.SetDateX(0.01)
    # s.SetDateY(0.01)

    # For the statistics box:
    s.SetOptFile(0)
    s.SetOptStat(0) # To display the mean and RMS:   SetOptStat('mr')
    s.SetStatColor(ROOT.kWhite)
    s.SetStatFont(42)
    s.SetStatFontSize(0.025)
    s.SetStatTextColor(1)
    s.SetStatFormat('6.4g')
    s.SetStatBorderSize(1)
    s.SetStatH(0.1)
    s.SetStatW(0.15)
    # s.SetStatStyle(1001)
    # s.SetStatX(0)
    # s.SetStatY(0)

    # Margins:
    s.SetPadTopMargin(0.08)
    s.SetPadBottomMargin(0.135)
    s.SetPadLeftMargin(0.14)
    s.SetPadRightMargin(0.04)

    # For the Global title:
    s.SetOptTitle(1)
    s.SetTitleFont(42)
    s.SetTitleColor(1)
    s.SetTitleTextColor(1)
    s.SetTitleFillColor(10)
    s.SetTitleFontSize(0.052)
    # s.SetTitleH(0) # Set the height of the title box
    # s.SetTitleW(0) # Set the width of the title box
    # s.SetTitleX(0) # Set the position of the title box
    # s.SetTitleY(0.985) # Set the position of the title box
    # s.SetTitleStyle(1001)
    # s.SetTitleBorderSize(2)

    # For the axis titles:
    s.SetTitleColor(1, 'XYZ')
    s.SetTitleFont(42, 'XYZ')
    s.SetTitleSize(0.052, 'XYZ')
    s.SetTitleOffset(1.05, 'X')
    s.SetTitleOffset(1.30, 'Y')

    # For the axis labels:
    s.SetLabelColor(1, 'XYZ')
    s.SetLabelFont(42, 'XYZ')
    s.SetLabelOffset(0.005, 'XYZ')
    s.SetLabelSize(0.0425, 'XYZ')

    s.SetPadTickX(1)
    s.SetPadTickY(1)

    s.cd()

    return

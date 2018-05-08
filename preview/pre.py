#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Sergey.Vinogradov@noaa.gov
"""
import os,sys
import argparse
import csdlpy
import datetime
import glob
import numpy as np
# Move to plot.py
import matplotlib
matplotlib.use('Agg',warn=False)
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates

#==============================================================================
def timestamp():
    print '------'
    print '[Time]: ' + str(datetime.datetime.utcnow()) + ' UTC'
    print '------'

#==============================================================================
def read_cmd_argv (argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('-w','--trackPath',      required=True)
    parser.add_argument('-i','--stormID',        required=True)
    parser.add_argument('-c','--stormCycle',     required=True)
    parser.add_argument('-o','--outputDir',      required=True)
    parser.add_argument('-t','--tmpDir',         required=True)
    parser.add_argument('-p','--pltCfgFile',     required=True)
    parser.add_argument('-u','--ftpLogin',       required=True)
    parser.add_argument('-f','--ftpPath',        required=True)

    args = parser.parse_args()
    print '[info]: hsofs preView is configured with :', args
    return args

#==============================================================================
def run_preview(argv):

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from preview import plot

    #Receive command line arguments
    args = read_cmd_argv(argv)

    # Read plotting parameters
    pp = csdlpy.plotter.read_config_ini (args.pltCfgFile)
    timestamp()

    # Try to create tmp directory
    if not os.path.exists(args.tmpDir):
        print '[warn]: tmpDir='+args.tmpDir+' does not exist. Trying to mkdir.'
        try:
            os.makedirs(args.tmpDir)
        except:
            print '[warn]: cannot make tmpDir=' +args.tmpDir
            args.tmpDir = os.path.dirname(os.path.realpath(__file__))
            print '[warn]: look for your output in a current dir='+args.tmpDir


    #Locate hsofs preview path
    hsofsPath = args.trackPath + args.stormID +'/'
    if not os.path.exists(hsofsPath):
        print '[error]: hsofs path ' +hsofsPath+ ' does not exist. Exiting'
        return

    ens_veer   = [] #Compile the list of available ensemble members
    ens_size   = []
    ens_vmax   = []

    pattern = hsofsPath + 'hsofs.' + args.stormID + '.' + \
                    args.stormCycle + '*.surfaceforcing'

    fls   = glob.glob( pattern )
    for f in fls:
        #s = os.path.basename(f).split('.')
        #ens.append(s[3] +'.'+ s[4] +'.'+ s[5] +'.'+ s[6])
        if 'ofcl' in f:
            advTrkFile = f
        if 'Rmax' in f:
            ens_size.append(f)
        if '.shift' in f:
            ens_veer.append(f)
        if 'Wind' in f:
            ens_vmax.append(f)
    print '[info]: ', str(len(ens_veer)),' hsofs preview veer ensembles detected.'
    print '[info]: ', str(len(ens_size)),' hsofs preview size ensembles detected.'
    print '[info]: ', str(len(ens_vmax)),' hsofs preview vmax ensembles detected.'


    # Define local files
    gridFile      = os.path.join(args.tmpDir,'fort.14')
    coastlineFile = os.path.join(args.tmpDir,'coastline.dat')
    citiesFile    = os.path.join(args.tmpDir,'cities.csv')


    timestamp()
    # Download files if they do not exist
    #csdlpy.transfer.download (      pp['Grid']['url'],      gridFile)
    csdlpy.transfer.download ( pp['Coastline']['url'], coastlineFile)
    csdlpy.transfer.download (    pp['Cities']['url'],    citiesFile)

    timestamp()
    #grid   = csdlpy.adcirc.readGrid(gridFile)
    coast  = csdlpy.plotter.readCoastline(coastlineFile)

    # Read tracks
    tracks_veer = []
    tracks_size = []
    tracks_vmax = []

    for e in ens_veer:
        tracks_veer.append( csdlpy.atcf.read.track( e) )
    for e in ens_size:
        tracks_size.append( csdlpy.atcf.read.track( e) )
    for e in ens_vmax:
        tracks_vmax.append( csdlpy.atcf.read.track( e) )

    advTrk = csdlpy.atcf.read.track(advTrkFile)

    # Plot
    plotFile = args.outputDir + args.stormID + '.' + args.stormCycle + '-veer-preview.png'
    titleStr = args.stormID + '.' + args.stormCycle+' veer perturbations.'
    plot.tracks ( advTrk, tracks_veer, coast, pp, titleStr, plotFile)
    csdlpy.transfer.upload (plotFile, args.ftpLogin, args.ftpPath)

    plotFile = args.outputDir + args.stormID + '.' + args.stormCycle + '-size-preview.png'
    titleStr = args.stormID + '.' + args.stormCycle+' size perturbations.'
    plot.size ( advTrk, tracks_size, coast, pp, titleStr, plotFile)
    csdlpy.transfer.upload (plotFile, args.ftpLogin, args.ftpPath)

    plotFile = args.outputDir + args.stormID + '.' + args.stormCycle + '-vmax-preview.png'
    titleStr = args.stormID + '.' + args.stormCycle+' vmax perturbations.'
    plot.vmax ( advTrk, tracks_vmax, coast, pp, titleStr, plotFile)
    csdlpy.transfer.upload (plotFile, args.ftpLogin, args.ftpPath)

#==============================================================================
if __name__ == "__main__":

    timestamp()
    run_preview (sys.argv[1:])
    timestamp()

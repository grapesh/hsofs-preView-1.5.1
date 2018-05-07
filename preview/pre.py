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
def findLatestForecast (dirMask):
    '''
    Checks the latest issued .fst and .dat files on NHC ftp site
    Returns URLs to aDeck and bDeck
    '''
    print '[error]: not yet implemented!'    
    #return aDeck, bDeck
    
#==============================================================================
def read_cmd_argv (argv):

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-w','--aswipPath',      required=True)
    parser.add_argument('-i','--stormID',        required=True)
    parser.add_argument('-c','--stormCycle',     required=True)
    parser.add_argument('-a','--aDeck',          required=True)    
    parser.add_argument('-b','--bDeck',          required=True)    
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
    from preView import plot
    
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



#==============================================================================    
if __name__ == "__main__":

    timestamp()
    run_preview (sys.argv[1:])
    timestamp()
    

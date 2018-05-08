import csdlpy
import numpy as np
import matplotlib
matplotlib.use('Agg',warn=False)
import matplotlib.pyplot as plt

#============================================================================
def tracks ( advTrk, tracks, coast, pp, titleStr, plotFile):

    # Default plotting limits, based on advisory track, first position
    lonlim = advTrk['lon'][0]-3.5, advTrk['lon'][0]+3.5
    latlim = advTrk['lat'][0]-0.5, advTrk['lat'][0]+6.5
    try:
        lonlim = float(pp['Limits']['lonmin']),float(pp['Limits']['lonmax'])
        latlim = float(pp['Limits']['latmin']),float(pp['Limits']['latmax'])
        clim   = float(pp['Limits']['cmin']),  float(pp['Limits']['cmax'])
    except: #default limits, in case if not specified in ini file
        pass

    f = csdlpy.plotter.plotMap(lonlim, latlim, fig_w=10., coast=coast)
    ax = f.gca()

    csdlpy.atcf.plot.track(ax, advTrk, color='k',linestyle='--',markersize=1,zorder=11)

    for t in tracks:
        csdlpy.atcf.plot.track(ax, t, color='r',linestyle='--',markersize=1,zorder=10)

    try:
        csdlpy.plotter.save(titleStr, plotFile)
    except:
        print '[error]: cannot save maxele figure.'

    plt.close(f)

#==============================================================================
def size ( advTrk, tracks, coast, pp, titleStr, plotFile):

    # Default plotting limits, based on advisory track, first position
    lonlim = advTrk['lon'][0]-3.5, advTrk['lon'][0]+3.5
    latlim = advTrk['lat'][0]-0.5, advTrk['lat'][0]+6.5
    try:
        lonlim = float(pp['Limits']['lonmin']),float(pp['Limits']['lonmax'])
        latlim = float(pp['Limits']['latmin']),float(pp['Limits']['latmax'])
        clim   = float(pp['Limits']['cmin']),  float(pp['Limits']['cmax'])
    except: #default limits, in case if not specified in ini file
        pass

    f = csdlpy.plotter.plotMap(lonlim, latlim, fig_w=10., coast=coast)
    ax = f.gca()

    csdlpy.atcf.plot.track(ax, advTrk, color='k',linestyle='--',markersize=1,zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq64', color='k',zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq50', color='k',zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq34', color='k',zorder=11)

    for t in tracks:
        csdlpy.atcf.plot.track(ax, t, color='r',linestyle='--',markersize=1,zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq64', color='r',zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq50', color='r',zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq34', color='r',zorder=10)

    try:
        csdlpy.plotter.save(titleStr, plotFile)
    except:
        print '[error]: cannot save maxele figure.'

    plt.close(f)

#==============================================================================
def vmax ( advTrk, tracks, coast, pp, titleStr, plotFile):

    # Default plotting limits, based on advisory track, first position
    lonlim = advTrk['lon'][0]-3.5, advTrk['lon'][0]+3.5
    latlim = advTrk['lat'][0]-0.5, advTrk['lat'][0]+6.5
    try:
        lonlim = float(pp['Limits']['lonmin']),float(pp['Limits']['lonmax'])
        latlim = float(pp['Limits']['latmin']),float(pp['Limits']['latmax'])
        clim   = float(pp['Limits']['cmin']),  float(pp['Limits']['cmax'])
    except: #default limits, in case if not specified in ini file
        pass

    f = csdlpy.plotter.plotMap(lonlim, latlim, fig_w=10., coast=coast)
    ax = f.gca()

    csdlpy.atcf.plot.track(ax, advTrk, color='k',linestyle='--',markersize=1,zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq64', color='k',zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq50', color='k',zorder=11)
    csdlpy.atcf.plot.size (ax, advTrk, 'neq34', color='k',zorder=11)

    for t in tracks:
        csdlpy.atcf.plot.track(ax, t, color='r',linestyle='--',markersize=1,zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq64', color='r',zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq50', color='r',zorder=10)
        csdlpy.atcf.plot.size (ax, t, 'neq34', color='r',zorder=10)

    try:
        csdlpy.plotter.save(titleStr, plotFile)
    except:
        print '[error]: cannot save maxele figure.'

    plt.close(f)


        



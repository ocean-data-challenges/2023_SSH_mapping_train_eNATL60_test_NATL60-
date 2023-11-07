import xarray as xr
import numpy
import matplotlib.pylab as plt
from matplotlib.ticker import ScalarFormatter


def plot_psd_score(ds):

    plt.figure(figsize=(8, 6))
    ax = plt.gca()
    #ax.invert_yaxis()
    #ax.invert_xaxis()
    c1 = plt.contourf(1./(ds['freq_lon']), 1./ds['freq_time'], ds['psd_score'],
                      levels=numpy.arange(0,1.1, 0.1), cmap='RdYlGn', extend='both')
    cbar = plt.colorbar(pad=0.01)
    plt.xlabel('spatial wavelenght (degree_lon)', fontweight='bold', fontsize=20)
    plt.ylabel('temporal wavelenght (days)', fontweight='bold', fontsize=20)
    #plt.xscale('log')
    #plt.yscale('log')
    plt.grid(linestyle='--', lw=1, color='w')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.title('PSD-based score', fontweight='bold', fontsize=20)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())
    c2 = plt.contour(1./(ds['freq_lon']), 1./ds['freq_time'], ds['psd_score'], levels=[0.5], linewidths=2, colors='k')
    cbar.add_lines(c2)

    bbox_props = dict(boxstyle="round,pad=0.5", fc="w", ec="k", lw=2)
    ax.annotate('Resolved scales',
            xy=(1.15, 0.8),
            xycoords='axes fraction',
            xytext=(1.15, 0.55),
            bbox=bbox_props,
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='center')

    ax.annotate('UN-resolved scales',
            xy=(1.15, 0.2),
            xycoords='axes fraction',
            xytext=(1.15, 0.45),
            bbox=bbox_props,
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='center')

    plt.show()

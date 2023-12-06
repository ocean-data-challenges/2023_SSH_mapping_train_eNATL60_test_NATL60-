import xarray as xr
import numpy
import matplotlib.pylab as plt
from matplotlib.ticker import ScalarFormatter


def plot_psd_score(ds_psd, time_min=5, time_max=35, step_time=5):
    
    nb_experiment = len(ds_psd.experiment)
        
    if nb_experiment > 1 :
        fig, ax0 =  plt.subplots(1, nb_experiment, sharey=True, figsize=(20, 5))
    else:
        fig, ax0 =  plt.subplots(1, nb_experiment, sharey=True, figsize=(10, 5))
    for exp in range(nb_experiment):
        try:
            ctitle = ds_psd.experiment.values[exp]
        except:
            ctitle = ''

        if nb_experiment > 1:
            ax = ax0[exp]
        else:
            ax = ax0
        data = (ds_psd.isel(experiment=exp).values)
        ax.invert_xaxis()
        c1 = ax.contourf(1./(ds_psd.freq_lon), 1./ds_psd.freq_time, data,
                          levels=numpy.arange(0,1.1, 0.1), cmap='RdYlGn', extend='both')
        ax.set_xlabel('spatial wavelength (degree_lon)', fontweight='bold', fontsize=18)
        
        if nb_experiment > 1:
            ax0[0].set_ylabel('temporal wavelength (days)', fontweight='bold', fontsize=18)
        else:
            ax0.set_ylabel('temporal wavelength (days)', fontweight='bold', fontsize=18)
        #ax.set_xscale('log')
        #ax.set_yscale('log')
        ax.grid(linestyle='--', lw=1, color='w')
        
        yticks = numpy.arange(time_min,time_max, step_time)
        xticks = numpy.arange(0, 15, 1)
        
        #ax.tick_params(axis='both', labelsize=18)
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.set_ylim(time_min,time_max)
      
        ax.set_title(f'PSD-based score ({ctitle})', fontweight='bold', fontsize=18)
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_formatter(ScalarFormatter())
        c2 = ax.contour(1./(ds_psd.freq_lon), 1./ds_psd.freq_time, data, levels=[0.5], linewidths=2, colors='k')

        cbar = fig.colorbar(c1, ax=ax, pad=0.01)
        cbar.add_lines(c2)

    bbox_props = dict(boxstyle="round,pad=0.5", fc="w", ec="k", lw=2)

    if nb_experiment > 1:
        ax0[-1].annotate('Resolved scales',
                        xy=(1.2, 0.8),
                        xycoords='axes fraction',
                        xytext=(1.2, 0.55),
                        bbox=bbox_props,
                        arrowprops=
                            dict(facecolor='black', shrink=0.05),
                            horizontalalignment='left',
                            verticalalignment='center')

        ax0[-1].annotate('UN-resolved scales',
                        xy=(1.2, 0.2),
                        xycoords='axes fraction',
                        xytext=(1.2, 0.45),
                        bbox=bbox_props,
                        arrowprops=
                        dict(facecolor='black', shrink=0.05),
                            horizontalalignment='left',
                            verticalalignment='center')
    else:
        ax0.annotate('Resolved scales',
                        xy=(1.2, 0.8),
                        xycoords='axes fraction',
                        xytext=(1.2, 0.55),
                        bbox=bbox_props,
                        arrowprops=
                            dict(facecolor='black', shrink=0.05),
                            horizontalalignment='left',
                            verticalalignment='center')

        ax0.annotate('UN-resolved scales',
                        xy=(1.2, 0.2),
                        xycoords='axes fraction',
                        xytext=(1.2, 0.45),
                        bbox=bbox_props,
                        arrowprops=
                        dict(facecolor='black', shrink=0.05),
                            horizontalalignment='left',
                            verticalalignment='center')
        
    plt.show()

    
def plot_psd_score_seasonal(ds_psd, time_min=5, time_max=35, step_time=5, order_mosaic={0:[0,0],1:[0,1],2:[1,0],3:[1,1]}):
    
    nb_experiment = 4
    
    fig, ax0 =  plt.subplots(2, 2, sharey=True, figsize=(20,15))
    #plt.subplots_adjust(right=0.1, left=0.09)
    for exp in range(nb_experiment):
        try:
            ctitle = ds_psd.experiment.values[exp]
        except:
            ctitle = ''

        ax = ax0[order_mosaic[exp][0],order_mosaic[exp][1]]
        data = (ds_psd.isel(experiment=exp).values)
        # ax.invert_yaxis()
        ax.invert_xaxis()
        c1 = ax.contourf(1./(ds_psd.freq_lon), 1./ds_psd.freq_time, data,
                          levels=numpy.arange(0,1.1, 0.1), cmap='RdYlGn', extend='both')
        ax.set_xlabel('spatial wavelength (degree_lon)', fontweight='bold', fontsize=18)
        
        ax0[0,0].set_ylabel('temporal wavelength (days)', fontweight='bold', fontsize=18)
        ax0[1,0].set_ylabel('temporal wavelength (days)', fontweight='bold', fontsize=18)
        #ax.set_xscale('log')
        #ax.set_yscale('log')
        ax.grid(linestyle='--', lw=1, color='w')
        
        yticks = numpy.arange(time_min,time_max, step_time)
        xticks = numpy.arange(0, 15, 1)
        
        #ax.tick_params(axis='both', labelsize=18)
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.set_ylim(time_min,time_max)
      
        ax.set_title(f'PSD-based score ({ctitle})', fontweight='bold', fontsize=18)
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_formatter(ScalarFormatter())
        c2 = ax.contour(1./(ds_psd.freq_lon), 1./ds_psd.freq_time, data, levels=[0.5], linewidths=2, colors='k')

        cbar = fig.colorbar(c1, ax=ax, pad=0.01)
        cbar.add_lines(c2)

    bbox_props = dict(boxstyle="round,pad=0.5", fc="w", ec="k", lw=2)

    for j in range(2):
        ax0[j,-1].annotate('Resolved scales',
                            xy=(1.2, 0.8),
                            xycoords='axes fraction',
                            xytext=(1.2, 0.55),
                            bbox=bbox_props,
                            arrowprops=
                                dict(facecolor='black', shrink=0.05),
                                horizontalalignment='left',
                                verticalalignment='center')

        ax0[j,-1].annotate('UN-resolved scales',
                            xy=(1.2, 0.2),
                            xycoords='axes fraction',
                            xytext=(1.2, 0.45),
                            bbox=bbox_props,
                            arrowprops=
                            dict(facecolor='black', shrink=0.05),
                                horizontalalignment='left',
                                verticalalignment='center')
        
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# function to plot a spectrum
# can choose to plot 1 or 2 by specifying the number - more can easily be added if required
# labels are for the legend
# ylog = True sets yscale to a log scale

def plot_spectrum(wav1, flux1, wav2, flux2, number = 1, 
                  flux_units = '(erg/cm2/s/Ang)', label1 = '', label2 = '', ylog = True, xlim = (1,1e5), wav_units = 'nm'):

    plt.figure(figsize = (12,5))
    
    if (number == 1):
        plt.plot(wav1, flux1, color = 'k', label = label1)
    elif (number == 2):
        plt.plot(wav1, flux1, color = 'k', label = label1)
        plt.plot(wav2, flux2, color = 'b', label = label2)
    plt.tick_params(labelsize = 15, width = 2, length = 4, right = True, top = True)
    plt.xlabel('Wavelength ' + '[' + wav_units + ']', fontsize = 15)
    plt.xscale('log')
    if (ylog == True):
        plt.yscale('log')
    plt.ylabel('Flux Density '+flux_units, fontsize = 15)
    plt.legend(loc = 0, frameon = False, fontsize = 15)
    plt.xlim(xlim)
    plt.show()
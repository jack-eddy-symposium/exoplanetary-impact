import numpy as np
from scipy.integrate import trapz
import spectres as sp

Irradiance_at_Earth = 1360000

def rebin_rescale(Wavelength,
                  model_wavelength, 
                  plot_Wavelength,
                  model, 
                  Scaled_flux_to_Earth,
                  starlabel,
                  flux_recieved_relative_to_Earth,
                  pl):
    
    # get maximum and minimum wavelength regions
    min_wav = np.argmin(abs(Wavelength-model_wavelength[0]))
    max_wav = np.argmin(abs(plot_Wavelength[-1]-model_wavelength))

    TSI_spectra_muscles = trapz(Scaled_flux_to_Earth[min_wav:], Wavelength[min_wav:])
    if (model == 'WACCM'):
        print('Total stellar irradiance from Muscles spectra is: ' + \
              str(round(TSI_spectra_muscles,2))+ ' mW/m^2/nm')
    elif (model == 'ROCKE-3D'):
        print('Total stellar irradiance from Muscles spectra is: ' + \
              str(TSI_spectra_muscles)+ ' mW/m^3')
    new_wav_grid = model_wavelength[:max_wav]
    New_grid_flux = sp.spectres(new_wav_grid, plot_Wavelength, Scaled_flux_to_Earth, spec_errs=None)
    TSI_spectra_model = trapz(New_grid_flux, new_wav_grid)

    print('Total stellar irradiance from ' + starlabel + ' spectra is: ' + \
          str(round(TSI_spectra_model,2))+ ' mW/m^2')

    print('Ratio of MUSCLES spectra to  ' + starlabel + ' spectra is: ' + \
          str(round(TSI_spectra_muscles/TSI_spectra_model,6)))

    # rescale to planet based on stellar luminoisty and semi-major axis from the NASA exoplanet archive
    Initial_scaled_flux = New_grid_flux * flux_recieved_relative_to_Earth
    TSI_spectra = trapz(Initial_scaled_flux, new_wav_grid)
    print('Scaled total stellar irradiance relative to the Sun: '+ str(TSI_spectra/Irradiance_at_Earth))

    ## Extend spectra using Raleigh Jeans Law
    #add in functionality with PHOENIX for later
    k = 1.381e-23
    c = 299792458
    T = pl['st_teff'].iloc[-1]
    scaling = Initial_scaled_flux[max_wav-1]
    RJL = 2*c*k*T/((model_wavelength[max_wav]*1e-9)**4)

    IR_scaling = scaling/RJL
    RJL_scaling = (IR_scaling)*(2*c*k*T/((model_wavelength*1e-9)**4))

    Flux = np.append(Initial_scaled_flux, RJL_scaling[max_wav:])

    RJL = 2*c*k*T/((new_wav_grid[-1]*1e-9)**4)

    # after adding in IR through Rayleigh Jeans law, provide final scaling 
    # this should not be a large factor (<1% difference) if model includes wavelengths up to 10,000 nm
    # however, note that it would be more realistic to use the PHOENIX code for this extension

    final_scaling = flux_recieved_relative_to_Earth/(trapz(Flux, model_wavelength) / Irradiance_at_Earth)
    Final_scaled_flux = final_scaling*Flux
    Final_scaled_flux = Final_scaled_flux.clip(min=0) #removes negative values
    return Final_scaled_flux
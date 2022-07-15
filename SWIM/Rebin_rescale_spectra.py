import numpy as np
from scipy.integrate import trapz
import spectres as sp

Irradiance_at_Earth = 1360000

def rebin_rescale(Wavelength,
                  model_wavelength, 
                  model, 
                  Scaled_flux_to_Earth,
                  starlabel,
                  pl, 
                  planet_name):
    
    #find semi-major axis in AU
    pl = pl.sort_values(by=['rowupdate'])
    semi_major_axis = pl['pl_orbsmax'].iloc[-1]
    print('semi-major axis of '+planet_name+' = '+str(semi_major_axis)+' AU')

    #find solar luminosity relative to Sun
    stellar_luminosity = 10**pl['st_lum'].iloc[-1]
    print('Star has '+str(stellar_luminosity)+ ' times luminosity of Sun')

    #find the flux recieved relative to Earth
    flux_recieved_relative_to_Earth = stellar_luminosity/(semi_major_axis**2)
    print(planet_name+' recieves '+str(flux_recieved_relative_to_Earth)+ \
          ' times flux recieved by Earth\n')
    
    # get maximum and minimum wavelength regions
    min_wav = np.argmin(abs(Wavelength-model_wavelength[0]))
    max_wav = np.argmin(abs(Wavelength[-1]-model_wavelength))

    new_wav_grid = model_wavelength[:max_wav]
    New_grid_flux = sp.spectres(new_wav_grid, Wavelength, Scaled_flux_to_Earth, spec_errs=None)
    TSI_spectra_model = trapz(New_grid_flux, new_wav_grid)

    print('Total stellar irradiance from ' + starlabel + ' spectra is: ' + \
          str(round(TSI_spectra_model,2))+ ' mW/m^2')

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
    return Final_scaled_flux, flux_recieved_relative_to_Earth
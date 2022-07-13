import os
import numpy as np
import xarray as xr

# function to read in a climate model solar spectral irradiance and its grid
# input: 
#    model name
# output:
#    irradiance (units: mW/m2)
#    grid (units: nm)
#    name of stellar object

def model_spectrum(model):

    #certain exoplanet/climate models require different files types

    unavailable = False
    
    flux_units = 'mW/m2/nm'
    
    if (model == 'WACCM' or model == 'CAM'):
        solar_file = 'SolarForcingCMIP6piControl_c160921.nc'
        #check for file. Download if not in directory
        if(os.path.isfile(solar_file)): 
            print('File already downloaded')
        else: 
            url = 'https://svn-ccsm-inputdata.cgd.ucar.edu/trunk/inputdata/atm/cam/solar/'
            os.system('wget '+url+solar_file+' --no-check-certificate')
    
        #read in file
        ds = xr.open_dataset(solar_file)#attach file to dataset
        ssi = ds['ssi'].isel(time=0) #define dataset from file
        model_flux = ssi.values #flux values
        model_wavelength = ssi.wavelength.values #wavelength grid
        starlabel = 'Sun' #label for plot
        flux_units = 'mW/m2/nm'
    
    elif(model == 'ExoCAM'):
        print('ExoCam spectrum input file unknown')
        unavailable = True
        flux_units = ''
    
    elif(model == 'UM'):
        print('UM spectrum input file unknown')
        unavailable = True
        flux_units = ''
    
    elif(model == 'LMD-G'):
        print('LMD-G spectrum input file unknown')
        unavailable = True
        flux_units = ''
    
    elif(model == 'ROCKE-3D'):
        #check for file. Download if not in directory
        if(os.path.isfile('sun')): 
            print('File already downloaded')
        else: 
            os.system('wget https://portal.nccs.nasa.gov/GISS_modelE/ROCKE-3D/stellar_spectra/sun')
        
        # note Wavelength is in m, Irradiance is (W/m3)
        ROCKE_3D_solar_input = np.genfromtxt('sun', skip_header = 5, skip_footer = 1)
        model_flux = ROCKE_3D_solar_input[:,1]*1e-6 # (mW/m2/nm)
        model_wavelength =  ROCKE_3D_solar_input[:,0]*1e9 # wavelength grid to nm
        starlabel = 'Sun' #label for plot
        
        flux_units = 'W/m3'
    
    elif(model == 'CCSM3'):
        print('CCSM3 spectrum input file unknown')
        unavailable = True
    
    elif(model == 'Atmos'):
        solar_file = 'muscles_gj667c.txt'  
        if(os.path.isfile(solar_file)): 
            print('File already downloaded')
        else:
            url = 'https://raw.githubusercontent.com/VirtualPlanetaryLaboratory/atmos/master/PHOTOCHEM/DATA/FLUX/'
            os.system('wget '+url+solar_file)
        ATMOS_gj667c_input = np.genfromtxt(solar_file)
        model_wavelength = ATMOS_gj667c_input[:,0]*0.1
        model_flux = ATMOS_gj667c_input[:,1]
        starlabel = 'GJ 667 C'
        flux_units = ''
    
    else:
        print('Spectrum input file unknown')
        
    if  unavailable:
        model_flux = 0.0
        model_wavelength = 0.0
        starlabel = 'n/a'

    return model_flux, model_wavelength, starlabel, flux_units
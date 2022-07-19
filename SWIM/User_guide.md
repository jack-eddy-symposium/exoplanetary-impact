# SWIM: User guide

## Authors and contributers:

<p>Gregory Cooke (University of Leeds, pygjc@leeds.ac.uk)</p>

## User Guide

To run the SWIM code, you first need to clone the repository. Open a terminal and navigate to where you would like the code to be placed. 

Now type: git clone https://github.com/jack-eddy-symposium/exoplanetary-impact.git

Once you have the repository on your local machine, open up a Jupyter notebook. There are multiple ways to do this. See [https://jupyter.org/install](https://jupyter.org/install) for Jupyter Notebook installation.

### Cell 1: Import required modules 
Run the first cell to import the necessary python libraries. If any errors occur at this step, then you lkely need to install some libraries. You may not have xarray, for example. In this case, in the terminal, run the following command: <i>conda install -c anaconda xarray</i>. Similar commands can be used to install other packages. See the packages at [https://anaconda.org/anaconda/](https://anaconda.org/anaconda/) for more details.

In the following cells, dropdown widgets will appear once the cell has been run.

### Cell 2: Access the MUSCLES database

For the data type selection, the final result should not depend too much on whether you select: \'Constant native resolution\', \'Variable native resolution\', \'Constant adaptive resolution\', or \'Variable adaptive resolution\'. However, if you want to compare to the original data, then select the format you require. A description of the formats can be found at [https://archive.stsci.edu/prepds/muscles/](https://archive.stsci.edu/prepds/muscles/).

### Cell 3: Select MUSCLES star

The list of stars in the MUSCLES database is listed. Select which star you would like to download the spectra for. 

### Cell 4: Read in MUSCLES data and assign to arrays 

This cell downloads and reads in the MUSCLES data. No options need to be selected.

### Cell 5: Select climate model for output

Run this cell and select the target model you would like to use. This will affect how the spectra will be rebinned and rescaled in order to be compatible with the model you have selected. If you do not see the model you would like to use, but you think SWIM would be useful for your model, please get in touch at pygjc@leeds.ac.uk.

### Cell 6: Assign wavelength grid from target model

This cell will download the wavelength and flux file needed for the target model if it is not already downloaded. The file will be used later for rebinning and saving out the final spectra file. No options are required to be selected.

### Cell 7: Access the Exoplanet Archive and choose exoplanet

Using the python library pandas, the notebook accessess the NASA exoplanet archive [https://exoplanetarchive.ipac.caltech.edu/](https://exoplanetarchive.ipac.caltech.edu/). the NASA exoplanet archive has several listings for each planet if there ate multiple observations. By default, the notebook selects the most recent update by sorting through the archive by when the row was last updated, and then selecting the fianl row:

<i>#find semi-major axis in AU

pl = pl.sort_values(by=['rowupdate'])

semi_major_axis = pl['pl_orbsmax'].iloc[-1]</i>

If you would like a different selection, you may want to alter the code in Rebin_rescale_spectra.py.

You should now have a list of planets that orbit the star you originally selected from the MUSCLES database. If you want to select a planet around a different star, but keep the same spectra, then set Spectra_name_same_as_host_name to <i>False</i>

### Cell 8: Rebin spectra to target model and rescale to exoplanet irradiance

This cell rebins and rescales the spectra to the necessary irradiance at the chosen planet. The code for doing this is in Rebin_rescale_spectra.py.


### Cell 9: Plot scaled spectra

Running this cell will plot the spectrum next to the spectrum of the Sun for comparioson. Plot_spectrum.py contains the code for this. If you are happy that eveverything looks good, move onto the next cell to save a file of this spectrum for your chosen model.

### Cell 11: Save spectrum to file

This cell will write the new rescaled and rebinned spectrum to a file containing a wavelength grid with flux values. We plan to add in detailed metadata for each file that is saved out.

### Cell 12: Clean up directory

This cell cleans up the directory and removes any .fits files that were downloaded from the MUSCLES website. Do not run if you would like to view them.



[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg



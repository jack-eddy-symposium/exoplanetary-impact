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

### Cell 5:

### Cell 6:

### Cell 7:

### Cell 8:

### Cell 9:

### Cell 10:

### Cell 11:



[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg



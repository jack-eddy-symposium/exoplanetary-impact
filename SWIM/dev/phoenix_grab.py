import os
from urllib import urlretrieve
import numpy as np

phxrepo = 'ftp://phoenix.astro.physik.uni-goettingen.de/HiResFITS/PHOENIX-ACES-AGSS-COND-2011'

# the husser spetra cover a grid with irregular step size in Teff and FeH, so I just explicitly duplicate the grids here
param_grids = {'Teff': np.hstack([np.arange(2300,7000,100), np.arange(7000,12001,200)]),
               'logg': np.arange(0.0, 6.1, 0.5),
               'FeH': np.hstack([np.arange(-4.0, -2.0, 1.0),  np.arange(-2.0, 1.1, 0.5)]),
               'a': np.arange(-0.2, 1.3, 0.2)}

def phxurl(Teff, logg=4.5, FeH=0.0, a=0.0):
    """
    Return the URL of a PHOENIX file for the appropriate parameters.
    """

    # check that all parameters are in the Husser grid.
    params = locals()   # get a dictionary of the function arguments/keywords
    for key, value in params.iteritems():
        grid = param_grids[key]
        if value not in grid:
            i = np.argmin(np.abs(value - grid))
            ival = grid[i]
            raise ValueError('{key} = {val} is not available in the Husser+ 2013 PHOENIX grid. Nearest value in '
                             'their grid, is {key} = {ival}.'.format(key=key, val=value, ival=ival))

    # the files in the FTP have some quirks in the names that these statemetns address
    FeH_str = '{:+4.1f}'.format(FeH)
    if FeH == 0.0: FeH_str = '-' + FeH_str[1:]
    a_str = '.Alpha={:+5.2f}'.format(a) if a != 0.0 else ''

    name = 'lte{T:05.0f}-{g:4.2f}{z}{a}.PHOENIX-ACES-AGSS-COND-2011-HiRes.fits'.format(T=Teff, g=logg, z=FeH_str, a=a_str)
    folder_name = 'Z{}{}'.format(FeH_str, a_str)
    return os.path.join(phxrepo, folder_name, name)


def fetchphxfile(Teff, logg, FeH, aM, savepath):
    """
    Grab a phoenix file and save to disk.
    """

    ftp_url = phxurl(Teff, logg, FeH, aM)
    urlretrieve(ftp_url, savepath)
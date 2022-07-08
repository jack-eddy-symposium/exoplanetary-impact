# SWIM: Stellar Wind and Irradiance Module

Created on June 6th 2022 @ 3rd Eddy Cross Disciplinary Symposium, Vail, CO, USA.
Code based on original idea by Dan Marsh (NCAR, University of Leeds).

## Authors and contributers:

Gregory Cooke (University of Leeds, pygjc@leeds.ac.uk)
Allison Youngblood (NASA Goddard)
Caitlin Gough (University of Leeds)
James Colliander (University of British Columbia)
Fernando Pérez (University of California, Berkeley)
Meng Lin (Lockheed Martin Solar & Astrophysics Lab / SETI Institute)
Dan Marsh (NCAR, University of Leeds)

## User Guide

Code to read in files from the MUSCLES database and scale them to be used in 
various atmospheric models for different planets in those stellar systems.
Run each cell until drop down menus appear.
Select your desired options from dropdown menus.
A file with wavelength and flux will be saved out.
This is a .nc (netCDF file) for CAM/WACCM, for example.

## To do list (community input required)
- Add in stellar wind models
- Add different climate model wavelength grids (only WACCM, ROCKE-3D, custom grids - and possibly Atmos - so far)
- These wavelength grids are not known to us (we could not find them)
- Add in different ways to save the data (e.g. files such as .csv, .txt etc.) to be compatable with different models


[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

This is the repository for projects in the "(Exo)Planetary Atmosphere: the Impact of Stars and Solar Physics on Habitability and Life" for the 3rd Jack Eddy Symposium. It is a place for scripts, issues, discussions, resources related to those projects

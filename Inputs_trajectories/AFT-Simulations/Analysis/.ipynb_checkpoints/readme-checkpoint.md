# Analysis of these large simulations is done in 3 stages

1. Creating files which contain the simulation snapshots in time, with the snapshots data converted to files by adding a point spread function to the 7S ends
2. Plotting these files to output '.tif' images which can be read by AFT analysis tool, doi : 10.3389/fcomp.2021.745831
3. Using the AFT tool with same parameters as experiment, see below

Stage 1 and 2 are documented in folders 'PointSpread_Data_Creation' and 'PointSpread_Plotting' respectively. Point 3 is documented below


# The AFT tool (doi : 10.3389/fcomp.2021.745831) and parameters used, with conversion to experimental parameters used:

In experiment, images of 200 x 200 pixels = = 21.6 x 21.6 microns = 50 x 50 molecule lengths (1 molecule ~ 400nm)
In simulations, images 327 x 327 pixels = 164.5 x 164.5 sigma = 50 x 50 molecule lengths (1 molecule ~3.5sigma)

In experiment, window size = 33
In simulation, window size = 33*(327/200) = 54

This means that for experiment window size = 33 pixels = 3.57 microns, we use window size 54 pixels.
Number of neighbours averaged over stays the same as 4
The percentage overlap stays the same as 50
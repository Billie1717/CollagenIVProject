# Plotting the point spread data created via protocols described in PointSpread_Data_Creation

The python file 'PointSpreadPlotting.py' plots many timepoints at once of data in the form TIMEPOINT+"NoStretch7sSeed"+str(SEED)+"_NoRemodelSimple_test0_sigma"+str(SIGMA)+".txt" (this is the name of the data I used, can be any name of point spread file data)

Where TIMEPOINT is the time point, SEED is the simulation random seed and SIGMA is the width of the point spread function, sigma = 2.5 is used for this work. This file is a 2D grid which represents all the 7S ends as a point spread function. 'vvmax' is the parameter which specifies the maximum of the black and white heatplot that is created from the data. Set to 12 or 16 for the data in this work. vvmax=12 gives brighter images and vvmax = 16 gives darker images. datadir  = '/' specifies the directory of the point spread data.

Images will be saved in a folder specified by 'plotsdir  =/'

Some dependencies for image creation 

pandas, matplotlib, seaborn

(Here, using python environment)

$ python3 -m venv path/to/venv
$ ~/Scratch/Collagen/model_strict_tetramer/ImageAnalysis_July2024/path/to/venv/bin/pip install pandas
$ ~/Scratch/Collagen/model_strict_tetramer/ImageAnalysis_July2024/path/to/venv/bin/pip install matplotlib
$ ~/Scratch/Collagen/model_strict_tetramer/ImageAnalysis_July2024/path/to/venv/bin/pip install seaborn
$ ~/Scratch/Collagen/model_strict_tetramer/ImageAnalysis_July2024/path/to/venv/bin/python PointSpreadPlotting.py
# files in this folder convert a simulation 'dump' file to a data file which adds a point spread function to the 7S ends
The files created can be plotted as heatplots which makes mimick microscopy data


The file MetaPointSpreadNewTrial.py will send many files to be converted into this type, using cluster jobs

The file is run with two inputs: MetaPointSpreadNewTrial.py {trajdir} and {workingdir} which are the trajectory directories (containing many simulation dump data timepoints) and the directory in which you want the data to be saved. The python file PointSpreadSimple.py must already be in the workingdir for this meta python file to work

The file PointSpreadSimple.py is the one that converts files to 2D .txt files. It outputs 3 files, each with a different point spread function width (1.5,2.0,2.5). 
It must be run via :
python PointSpreadSimple.py ${Stretch} ${trajdir} ${filename} ${datadir} ${dataname}
Where Stretch is the amount the network gets stretched, trajdir is the trajectory directory, filename is the dump file name (of a specific timepoint), and datadir + dataname are the output data directories and data name. (The parameter 'stretch' is now redundant and not used in this file)



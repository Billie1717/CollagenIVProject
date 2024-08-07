# CollagenIVProject
This repository has all the code and instructions for a coarse-grained collagen IV model implemented in molecular dynamics using LAMMPS

## Folders explained

The folder /Lammps has instructions for which lammps version was used and with what additional edits to the source code.

The folder /Main_model has one lammps input script other dependencies for running a simulation where collagenIV protomers assemble. The input script is commented and from this folder one can understand the model.

The folder /Inputs_trajectories has the information for different kinds of simulation using this model. Here one can find the python scripts to make the inputs for different sorts of runs, assembly, assembly and stretch, large simulations, non-equilibrium vs equilibrium, x-and-y- stretching

The folder /Analysis contains the analysis code for various quantities which are plotted in the /Data_and_Figures folder

Lastly, the foler /Data_and_Figures has plotting scripts for various quantities (which are used in my thesis, and 3 manuscripts ** refs tbc **)


## Other notes


For updated git repo in local:

git remote add origin main https://<token>@github.com/Billie1717/CollagenIVProject
git push origin HEAD:master (instead of git push origin main)
git push origin master
git pull origin master ???
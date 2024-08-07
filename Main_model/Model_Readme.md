# Explaining the model

The model is run in lammps and uses the REACTION package. The reactions allow the changing of atom types depending on their bonding, allowing us to choose the sequence of bonding.


## atom-type changing templates

To change types depending on bonding, it is required to specify many atom templates which singles out atoms bonded in a certain way and changes their type accordingly. These are contained in the folder /templates. This folder is essential and must be kept in the same directory as the lammps input file for the simulations to run.

## initial conditions

The files lseed.dat and vseed.dat contain random numbers which set the initial random lengevin thermostat and initial random velocity, respectivly

## inital data file

The file 'data' contains a grid of non-bonded protomers all of type 1 and 2 in a simulation box 72x72x12. This example has 3125 protomers, 6250 atoms. 
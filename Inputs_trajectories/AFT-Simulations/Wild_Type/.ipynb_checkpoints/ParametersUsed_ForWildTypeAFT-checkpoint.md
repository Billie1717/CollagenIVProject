# The inputs required and typical parameters used for each simulation protocol:

Python files run by eg:

python3 build_StretchNonEquilib.py ${foldernameadd} ${t_mix} ${t_bonds} ${t_stretch} ${t_relax} ${NBM_Cyc} ${XStretch} ${k_angle} ${Nevery} ${Blen} ${MakeDist} ${BreakDist} ${MakeProb} ${BreakProb} ${seed}

In this folder, you can change/sweep parameters using the bash script runMakeNonEq.sh which will run the above python line

# The input config data for these large simulations is located in the folder:
 /Inputs_trajectories/Ablation_example/LargerSImulation_InputConfig/data

# For condition 1. No bond breaking + stretching

## build_StretchNonEquilib.py

Running this python script to create lammps input files requires the following inputs:

foldernameadd----- folder_name------ folder name for simulation 
t_mix------------- 1e5-------------- time to mix protomers in simulation steps 
t_bonds----------- 5e5-------------- time to make bonds in simulation steps 
t_stretch--------- 1e5-------------- time to stretch in simulation steps 
t_relax----------- 5e5-------------- time to relax in simulation steps 
NBM_Cyc----------- 100--------------- number of make and break bond cycles (actual number > as in relax = 5x NBM_cyc and make bonds 1x NBM_cyc)
XStretch---------- 350-------------- amount of stretch in x-dirction in simulation length units, vary between 72 (100%) and 144 (200%)
k_angle----------- 1.0-------------- Angular bond constant in kBT
Nevery------------ 500-------------- How often we check for breaking a bond, must be quite high to allow bonds to react (type change) in between. Vary between 200 and 500.
Blen-------------- 0.5-------------- Length of harmonic bond between protomers (in simulation units)
MakeDist---------- 1.3-------------- The factor of the bond length at which a bond is considered to be made (it will be considered at MakeDist * Blen)
BreakDist--------- 3.2-------------- The factor of the bond length at which a bond is considered to be broken (it will be considered at BreakDist * Blen) varies between {2.4,4}
MakeProb---------- 1.0-------------- The probability of making a bond between two protomers which are < MakeDist * Blen away. Varies between {0.01,1.0}
BreakProb--------- 0.0-------------- The probability of breaking a bond when it is > BreakDist * Blen away. Varies between {0.0001,0.01}
seed-------------- 1---------------- Random seed for - integer, for creating random seeds for initial velocity and lengevin thermostat


# For condition 2. Bond breaking + stretching

## build_StretchNonEquilib.py

Running this python script to create lammps input files requires the following inputs:

foldernameadd----- folder_name------ folder name for simulation 
t_mix------------- 1e5-------------- time to mix protomers in simulation steps 
t_bonds----------- 5e5-------------- time to make bonds in simulation steps 
t_stretch--------- 1e5-------------- time to stretch in simulation steps 
t_relax----------- 5e5-------------- time to relax in simulation steps 
NBM_Cyc----------- 100--------------- number of make and break bond cycles (actual number > as in relax = 5x NBM_cyc and make bonds 1x NBM_cyc)
XStretch---------- 350-------------- amount of stretch in x-dirction in simulation length units, vary between 72 (100%) and 144 (200%)
k_angle----------- 1.0-------------- Angular bond constant in kBT
Nevery------------ 500-------------- How often we check for breaking a bond, must be quite high to allow bonds to react (type change) in between. Vary between 200 and 500.
Blen-------------- 0.5-------------- Length of harmonic bond between protomers (in simulation units)
MakeDist---------- 1.3-------------- The factor of the bond length at which a bond is considered to be made (it will be considered at MakeDist * Blen)
BreakDist--------- 3.2-------------- The factor of the bond length at which a bond is considered to be broken (it will be considered at BreakDist * Blen) varies between {2.4,4}
MakeProb---------- 1.0-------------- The probability of making a bond between two protomers which are < MakeDist * Blen away. Varies between {0.01,1.0}
BreakProb--------- 0.003-------------- The probability of breaking a bond when it is > BreakDist * Blen away. Varies between {0.0001,0.01}
seed-------------- 1---------------- Random seed for - integer, for creating random seeds for initial velocity and lengevin thermostat


# For condition 3. Bond breaking + no stretching

## build_StretchNonEquilib.py

Running this python script to create lammps input files requires the following inputs:

foldernameadd----- folder_name------ folder name for simulation 
t_mix------------- 1e5-------------- time to mix protomers in simulation steps 
t_bonds----------- 5e5-------------- time to make bonds in simulation steps 
t_stretch--------- 1e5-------------- time to stretch in simulation steps 
t_relax----------- 5e5-------------- time to relax in simulation steps 
NBM_Cyc----------- 100--------------- number of make and break bond cycles (actual number > as in relax = 5x NBM_cyc and make bonds 1x NBM_cyc)
XStretch---------- 0-------------- amount of stretch in x-dirction in simulation length units, vary between 72 (100%) and 144 (200%)
k_angle----------- 1.0-------------- Angular bond constant in kBT
Nevery------------ 500-------------- How often we check for breaking a bond, must be quite high to allow bonds to react (type change) in between. Vary between 200 and 500.
Blen-------------- 0.5-------------- Length of harmonic bond between protomers (in simulation units)
MakeDist---------- 1.3-------------- The factor of the bond length at which a bond is considered to be made (it will be considered at MakeDist * Blen)
BreakDist--------- 3.2-------------- The factor of the bond length at which a bond is considered to be broken (it will be considered at BreakDist * Blen) varies between {2.4,4}
MakeProb---------- 1.0-------------- The probability of making a bond between two protomers which are < MakeDist * Blen away. Varies between {0.01,1.0}
BreakProb--------- 0.003-------------- The probability of breaking a bond when it is > BreakDist * Blen away. Varies between {0.0001,0.01}
seed-------------- 1---------------- Random seed for - integer, for creating random seeds for initial velocity and lengevin thermostat

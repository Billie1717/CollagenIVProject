# The 7s perturbations
These are simulations which have double the number of molecules as wild type, with half of the molecules having a inert 7S end which does not react to form bonds

- The input scripts are created with the following python file:

python3 build_SeededNonEquilib.py ${foldernameadd} ${t_mix} ${t_bonds} ${t_stretch} ${t_relax} ${NBM_Cyc} ${XStretch} ${k_angle} ${Nevery} ${Blen} ${MakeDist} ${BreakDist} ${MakeProb} ${BreakProb} ${seed}

The only difference is an exttra bead type (8) which does not take part in reactions/ bond making/breaking

- The input configuration is in this folder called 'data'

- You can make more/different 7s configuration files with the python script create_lattice7Spert.py

- We run with the same parameters as the bond breaking wild type:

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
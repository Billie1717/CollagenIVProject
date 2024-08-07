# For the Assembly Metrix Figures:

The /dumplin_bonds folder is from the remote directory:

'/nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTestStress/run_tmix1e4_tbonds1e5_tstretch1e4_trelax1e5_N_fix500_XStretch72_Nev500_ChemBond6.0_prob0.1_seed1/dumplin_bonds/'

Made in the equilibrium bond remodelling regime

Made with the input script 'collagen_assembly.in'


# For the Particle Types Figures:

xHistsLarge_tmix1e4_tbonds1e5_tstretch1e4_trelax1e5_N_fix500_XStretch72_Nev500_ChemBond6.0_prob0.1_seed1.txt

From the same simulation as above


Analysed using the analysis script:

Python Histogram_Types.py /simdirectory fileOut (

Which is in the analysis folder 




python /nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model2_dumbell/scripts/Analysis/Histogram_Types.py ${filepattern0} ${fileOut}
~/Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTestStress/run_tmix1e4_tbonds1e5_tstretch1e4_trelax1e5_N_fix500_XStretch72_Nev500_ChemBond6.0_prob0.1_seed1
filepattern0='/nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTestStress/run_tmix1e4_tbonds1e5_tstretch1e4_trelax1e5_N_fix500_XStretch72_Nev500_ChemBond6.0_prob0.1_seed1
echo ${filepattern0}
fileOut='/nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/Data/xHistsLarge_tmix'${t_mix}'_tbonds'${t_bonds}'_tstretch'${t_stretch}'_trelax'${t_relax}'_N_fix'${NBM_Cyc}'_XStretch'${XStretch}'_Nev'${Nevery}'_ChemBond'${ChemBond}'_prob'${prob}'_seed'${seed}'.txt'
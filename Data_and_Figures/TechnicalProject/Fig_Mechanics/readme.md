

*** need to write a bit about where this data comes from ***/ analysis

stress :


seeds = "3 4 6 7".split()
for s in range(len(seeds)):
    datadir  = '/nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTestStress/'
    
    foldername = datadir+'runBONDprinting_tmix1e4_tbonds5e5_tstretch1e4_trelax5e5_N_fix50_XStretch108_Nev200_ChemBond6.0_prob0.05_seed'+seeds[s]
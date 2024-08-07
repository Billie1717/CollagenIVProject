These relaxation plots are all from averaging 5 seeds with various chemical bond energies (3.0 4.0 5.0 6.0 7.0 100.0)
1 example input script in this folder : 'Example_Input_EquilibRelaxation_EB5.0.in'

The full runs are in the remote folder :
Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTauPhiSweep

And these are taken from stretching by '108'

For example, seed 1, EB 5 (150% stretch, 108 in sim units) : Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/runsTauPhiSweep/runBONDprinting_tmix1e4_tbonds1e5_tstretch1e4_trelax5e5_N_fix100_XStretch108_Nev500_ChemBond5.0_prob0.1_seed1/

The runs are then analysed with the Molecular Angle analysis script MoleculeAngle.py (in the Analys folder in the parent directory)

Which gives a text file, for example:
MoleculeAngleTauPhi_tmix1e4_tbonds1e5_tstretch1e4_trelax5e5_N_fix100_XStretch108_Nev500_ChemBond5.0_prob0.1_seed1.txt'

All these files are kept in the remote directory:
Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/Data/

We then average these over the seeds to get the average and standard given in this local /Data folder
Averaging is done in the remote script:
Scratch/Collagen/model_strict_tetramer/EquilibriumSeededWorkflow/Plotting/AlignmentAndFittingNEWEQ.ipynb



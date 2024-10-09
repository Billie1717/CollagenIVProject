#!/bin/bash
#module load python3/recommended
MakeDist=1.3
BreakDist=1.3
k_angle=1.0
NBM_Cyc=100
NeveryCr=1000
NeveryBr=1000
XStretch=72
BreakProb=0.0
BreakDist=1.3
Blen=0.5
MakeProb=1.0
t_mix=1e5
t_stretch=1e5
t_relax=5e5
t_bonds=5e5
NBM_Cyc=100
Nevery=500
for BreakDist in 3.2 #3.6 #400 300 200 100 #500
do
for BreakProb in 0.003 #0.001 #1000 #100 #500 1000 
do
for MakeProb in 1.0 #3.0 4.0 5.0 6.0 7.0 #5.0 6.0 #4.0 #3.0 4.0 5.0 6.0 #2.0 #5.0
do
for seed in 5 #7 8 9 10 #4 5 #3 4 5
do
for XStretch in 350 #72 108 144 #0.2
do
foldernameadd='runsLargeSimulations/run7SpertRestart_NONEQUIB_stretch_tmix'${t_mix}'_tbonds'${t_bonds}'_tstretch'${t_stretch}'_trelax'${t_relax}'_N_fix'${NBM_Cyc}'_XStretch'${XStretch}'_Nev'${Nevery}'_MP'${MakeProb}'_BP'${BreakProb}'_MD'${MakeDist}'_BD'${BreakDist}'_seed'${seed}
foldernameadd2='runsLargeSimulations/run7Spert_NONEQUIB_stretch_tmix'${t_mix}'_tbonds'${t_bonds}'_tstretch'${t_stretch}'_trelax'${t_relax}'_N_fix'${NBM_Cyc}'_XStretch'${XStretch}'_Nev'${Nevery}'_MP'${MakeProb}'_BP'${BreakProb}'_MD'${MakeDist}'_BD'${BreakDist}'_seed'${seed}
mkdir ${foldernameadd}
#input='dumbbells_7sPert_n16245_bl3.00_Lz12.00_rho5.000e-02.lammpsdata'
#input=${foldernameadd2}'/restart.poststretch'
input=${foldernameadd2}'/restart.postmakebonds'
#t_mix=1e2
#input='OrigLattice/restart.postmakebonds'
#cp ${input} ${foldernameadd}'/restart.postmakebonds'
#input='OrigLattice/data200'
cp ${input} ${foldernameadd}'/data.restart'
#cp ${input} ${foldernameadd}'/data'
cp -r 'templates' ${foldernameadd}
python3 build_SeededNonEquilibRestart.py ${foldernameadd} ${t_mix} ${t_bonds} ${t_stretch} ${t_relax} ${NBM_Cyc} ${XStretch} ${k_angle} ${Nevery} ${Blen} ${MakeDist} ${BreakDist} ${MakeProb} ${BreakProb} ${seed}
cd ${foldernameadd}
runscriptfile='runscript.sh'
sbatch $runscriptfile
cd .. 
cd ..
done
done
done
done
done

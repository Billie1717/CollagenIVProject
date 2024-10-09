#!/bin/bash
#module load python3/recommended
MakeDist=1.3
k_angle=1.0
Blen=0.5
t_mix=1e5
t_stretch=1e5
t_relax=5e5
t_bonds=5e5
NBM_Cyc=100
Nevery=500
for BreakDist in 3.2
do
for BreakProb in 0.003 
do
for MakeProb in 1.0 
do
for seed in 1
do
for XStretch in 108 
do
foldernameadd='runs_NoRemodel/runRestart_tmix'${t_mix}'_tbonds'${t_bonds}'_tstretch'${t_stretch}'_trelax'${t_relax}'_N_fix'${NBM_Cyc}'_XStretch'${XStretch}'_Nev'${Nevery}'_MP'${MakeProb}'_BP'${BreakProb}'_MD'${MakeDist}'_BD'${BreakDist}'_seed'${seed}
mkdir ${foldernameadd}
input='data'
cp ${input} ${foldernameadd}'/data'
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
from __future__ import division, print_function
import numpy as np
#import matplotlib.pyplot as plt
import math
import time
import random
import sys, getopt
import os
import subprocess

def main():

    ################ Parameters ################
    trajdir = str(sys.argv[2])
    workingdir = str(sys.argv[1])
    Frame = 2400
    Last = 1200000 ## THESE ARE NUMBERS FOR 'STRETCH' DATA
    First= 292*Frame #1034400 #722400 ## THESE ARE NUMBERS FOR 'STRETCH' DATA
    #Last = 400*Frame
    #Last = 292*Frame 
    #Last = 1200000
    First = 125*Frame ## THESE ARE NUMBERS FOR 'NO STRETCH' DATA
    Last = 489600 #251*Frame ## THESE ARE NUMBERS FOR 'NO STRETCH' DATA
    time = np.arange(First,Last,Frame*2)
    #time = np.arange(Frame,Last,Frame*10)

    time_strList=[]
    for i in range(len(time)):
        time_str = str(time[i])
        if len(time_str)<5:
            time_strList.append('000000'+time_str)
        elif len(time_str)<6:
            time_strList.append('00000'+time_str)
        elif len(time_str)<7:
            time_strList.append('0000'+time_str)
        else:
            time_strList.append('000'+time_str)

    ################ write in.local ################
    for t in range(len(time_strList)):
        #if time[t]<700000:
        stretch = 0
       # else:
       #     stretch = 350
        print('Writing PointSpread'+time_strList[t]+'.sh\n')
        outfile2 = workingdir +"/PointSpread"+time_strList[t]+".sh"
        fo=open(outfile2,'w')
        fo.write('''#!/bin/bash\n
#
''')
        fo.write('trajdir="'+trajdir+'"\n')
        fo.write('Stretch='+str(stretch)+'\n')
        fo.write('datadir="'+workingdir+'"\n')
        fo.write('filename="dump.run_T1.'+time_strList[t]+'.lammpstrj"\n')
        fo.write('dataname="'+time_strList[t]+'NoStretch"\n')
        fo.write('python PointSpreadSimple.py ${Stretch} ${trajdir} ${filename} ${datadir} ${dataname}')
        fo.close()

    ################ write runscript ################
        runscriptfilename =  workingdir +"/runscript"+time_strList[t]+".sh"
        print('Writing runscript.sh\n')
        f = open(runscriptfilename, "w")
        f.write(
            '''#!/bin/bash
#
#SBATCH -J Analysis
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=1G 
#SBATCH --time=06:00:00 
#SBATCH --mail-user=ucapbbm@ucl.ac.uk
#SBATCH --mail-type=END
#SBATCH --export=NONE 
''')
        f.write('#SBATCH --chdir='+workingdir+'\n')
        f.write(
            '''

module load lammps/20220623b
module load python
pip install ovito
''')
        f.write('bash PointSpread'+time_strList[t]+'.sh\n')
        f.close()
        command = 'sbatch '+runscriptfilename
        print(command)
        # Execute the command
        subprocess.run(command, shell=True)

##SBATCH --constraint="epsilon|delta|beta|leonid|serbyn|gamma"     
if __name__ == "__main__":
    main()

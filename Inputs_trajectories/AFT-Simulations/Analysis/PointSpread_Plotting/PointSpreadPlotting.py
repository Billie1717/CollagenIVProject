import sys
sys.path.append("..")
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import io

clrs = ['#a6611a','#dfc27d','#80cdc1','#018571','#f5f5f5']
datadir  = '/nfs/scistore15/saricgrp/bmeadowc/Scratch/Collagen/model_strict_tetramer/ImageAnalysis_July2024/7sPert_NEQSeed1/'
plotsdir  = datadir+'/Plots/'

sigmas = "2.5".split()
Frame = 2400
Last = 489600 + Frame*10 #955200+Frame*2 #700800 #955200 #600000 #722400 #722400 #600000 #1200000
First= 125*Frame #489600 #700800 #489600 #703200 #489600 #125*Frame # 489600 #916800 #489600 #600000 #480000 #578400 #578400 #600000 #722400 #962400 +Frame*20 #
Last = 489600 #1200000 #251*Frame #489600 + Frame*3 #1200000 #936000 + Frame*2 #955200+Frame*2 #700800 #955200 #600000 #722400 #722400 #600000 #1200000
time = np.arange(Frame,Last,Frame*10)
time = np.arange(First,Last,Frame*2)
StretchCount = 0
seed = "1".split()
vvmax = 12
#time = np.arange(First,Last,Frame*10)
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
fig2,ax2 = plt.subplots(1,len(sigmas),figsize = (8*len(sigmas),6))

for ss in range(len(seed)):
    for t in range(len(time_strList)):
        
        fig1,ax1 = plt.subplots(1,figsize = (4.22,4.25))
        
        sigmachosen = "2.5".split() #1.5 2.0 
        for s in range(1):
            fname1 = time_strList[t]+"NoStretch7sSeed"+str(seed[ss])+"_NoRemodelSimple_test0_sigma"+str(sigmachosen[s])+".txt"
            df = pandas.read_csv(datadir+fname1, sep = ' ',header =None)
            print(fname1)
             #12 
            sns.heatmap(df,ax=ax1, cmap="Greys_r",cbar=False,vmin = 0,vmax = vvmax,alpha=(1)) 
            ax1.invert_yaxis()
            plt.axis('off')
            plt.gca().set_frame_on(False)
            plt.gcf().set_facecolor('white')
            # Create your plot
            # Convert the Matplotlib figure to a PIL image
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
            buf.seek(0)
            img = Image.open(buf)

            # Convert to RGB mode (optional, only if the image is in RGBA mode)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            plotname = "NoStretch"+time_strList[t]+"Seed"+seed[ss]+"_stretchCount"+str(StretchCount)+"_sigma"+sigmachosen[s]+".tif"
            folder = "vvmax_const"+str(vvmax)+"_sigma"+sigmachosen[s]+"/"
            # Save the image without transparency
            img.save(plotsdir+folder+plotname,bbox_inches='tight', pad_inches=0)




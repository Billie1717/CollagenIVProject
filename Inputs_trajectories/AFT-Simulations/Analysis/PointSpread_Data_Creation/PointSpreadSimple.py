import sys
sys.path.append("..")
import pandas
import numpy as np
from ovito.io import *
from ovito.modifiers import *
from ovito.io import export_file
from ovito.data import *



datadir  = str(sys.argv[4])



def spreadzedNoStretch(x1,y,means,sigma1,sigma2,sigma3):
    z1 = np.zeros((len(y),len(x1)))
    z2 = np.zeros((len(y),len(x1)))
    z3 = np.zeros((len(y),len(x1)))
    print(y[0],y[-1],abs((y[-1]+y[0])))
    for i in range(len(x1)):
        #if i%(int(len(x1)/20))==0:
        #    print(i*100/len(x1),"% done")
        for j in range(len(y)):
            for m in range(len(means[0,:])):
                z1[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma1)**2+((y[j]-means[1,m])/sigma1)**2))
                z2[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma2)**2+((y[j]-means[1,m])/sigma2)**2))
                z3[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma3)**2+((y[j]-means[1,m])/sigma3)**2))
                if means[1,m] > abs((y[-1]+y[0])):
                    print("got here")
                    meansT = means[1,m]-y[-1]
                    z1[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma1)**2+((y[j]-meansT)/sigma1)**2))
                    z2[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma2)**2+((y[j]-meansT)/sigma2)**2))
                    z3[j,i] += np.exp(-(((x1[i]-means[0,m])/sigma3)**2+((y[j]-meansT)/sigma3)**2))
    return z1,z2,z3


def main():

    stretch = float(sys.argv[1])

    if stretch<350:
        stretchCount = 0 #int(stretch)
        stretch =0
    else:
        stretchCount = int(stretch)
    
    xhi = 1.6454482700000000*100 #+stretch/2
    xlo = 0 #-stretch/2
    yhi = 1.6454482700000000*100
    ylo = 0
    #if stretch<350:
    #    stretchCount = 0 #int(stretch)
    #else:
    #    stretchCount = int(stretch)
    #Construct new box:
    xtot = xhi-xlo
    #if stretchCount == 0:
    HalfXtot = xtot
    #else:
    #    HalfXtot = xtot/2
        
    #print(HalfXtot)
    xlo1 = xlo
    xhi1 = xlo+HalfXtot
    ylo1 = yhi-HalfXtot
    yhi1 = yhi
    #xlo2 = xhi1
    #xhi2 = xlo2+HalfXtot
    #print(xlo1,xhi1,xlo2,xhi2)
    
    print(ylo1,ylo,yhi,yhi1,xlo,xlo1,xhi,xhi1)
    
    
    NumPixels = 200
    sigma1 = 1.5
    sigma2 = 2.0
    sigma3 = 2.5
    trajdir = str(sys.argv[2])
    filename = str(sys.argv[3])
    print(trajdir+filename)
    # Data import:
    pipeline = import_file(trajdir+filename)
    # Wrap at periodic boundaries:
    pipeline.modifiers.append(WrapPeriodicImagesModifier())
    data = pipeline.compute()
    positions = data.particles['Position']
    types = data.particles['Particle Type']
    xcoords = positions[:, 0]
    ycoords = positions[:, 1]
    z_coordinates = positions[:, 2]
    print(len(xcoords))
    NumCoords = len(xcoords) #3215 #len(xcoords)
    #print(NumCoords)
    coords = np.zeros((2,int(NumCoords/2)))
    for j in range(NumCoords):
        if types[j] >1:
            #print("here")
            coords[0,int(j/2)] = xcoords[j]
            coords[1,int(j/2)] = ycoords[j]
    MeshX1 = np.linspace(xlo1,xhi1,NumPixels) #np.arange(xlo,xhi,0.5)
    #MeshX2 = np.linspace(xlo2,xhi2,NumPixels)
    MeshY = np.linspace(ylo1,yhi1,NumPixels)
    #if stretchCount==0:
    zspread1 = spreadzedNoStretch(MeshX1,MeshY,coords,sigma1,sigma2,sigma3)
    #else:
    #    zspread1 = spreadzedNoStretch(MeshX1,MeshY,coords,sigma1,sigma2,sigma3)
    #    zspread2 = spreadzedNoStretch(MeshX2,MeshY,coords,sigma1,sigma2,sigma3)
    filename = str(sys.argv[5]) 
    outfile1 = datadir+ filename+"7sSeed1_NoRemodelSimple_test"+str(stretchCount)+"_"
    #outfile2 = datadir+ filename+"7sSeed2_NoRemodelSimple_test"+str(stretchCount)+"_"
    f1 = open(outfile1+"sigma"+str(sigma1)+".txt",'w')    
    f2 = open(outfile1+"sigma"+str(sigma2)+".txt",'w')   
    f3 = open(outfile1+"sigma"+str(sigma3)+".txt",'w')  
    #if stretchCount!=0:
    #    v1 = open(outfile2+"sigma"+str(sigma1)+".txt",'w')    
    #    v2 = open(outfile2+"sigma"+str(sigma2)+".txt",'w')   
    #    v3 = open(outfile2+"sigma"+str(sigma3)+".txt",'w')   
    
    for j in range(len(MeshY)):
        if j!=0:
            f1.write('\n')
            f2.write('\n')
            f3.write('\n')
            #if stretchCount!=0:
            #    v1.write('\n')
            #    v2.write('\n')
            #    v3.write('\n')
        for i in range(len(MeshX1)):
            f1.write(str(zspread1[0][j][i])+" ")
            f2.write(str(zspread1[1][j][i])+" ")
            f3.write(str(zspread1[2][j][i])+" ")
            #if stretchCount!=0:
            ##    v1.write(str(zspread2[0][j][i])+" ")
             #   v2.write(str(zspread2[1][j][i])+" ")
              #  v3.write(str(zspread2[2][j][i])+" ")
    f1.close()
    f2.close()
    f3.close()
    #if stretchCount!=0:
    #    v1.close()
    #    v2.close()
    #    v3.close()
        
if __name__ == "__main__":
    main()

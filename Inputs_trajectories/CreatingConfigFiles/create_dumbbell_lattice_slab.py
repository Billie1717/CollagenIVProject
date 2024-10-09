#The unit of length is the particle diameter.

from numpy import *
from numpy.random import *

nmol0=int(input("Enter n. of molecules:"))
bond_length=float(input("Enter bond length:"))
density=float(input("Enter density:"))

lattice_z=2.
nmol_side_z=5

lattice_x=sqrt(1./(density*lattice_z)*(nmol_side_z/(nmol_side_z+1)))
lattice_y=lattice_x
nmol_side_x=int(sqrt(nmol0/(nmol_side_z+1)))
nmol_side_y=nmol_side_x

box_x=lattice_x*nmol_side_x
box_y=lattice_y*nmol_side_y
box_z=lattice_z*(nmol_side_z+1)

nmol=nmol_side_x*nmol_side_y*nmol_side_z
natoms=2*nmol

with open('dumbbells_lattice_slab_n%d_bl%.2f_Lz%.2f_rho%.3e.lammpsdata'%(nmol,bond_length,box_z,density),'w') as fout:
    fout.write("LAMMPS data file\n\n%d atoms\n%d bonds\n\n2 atom types\n1 bond types\n\n0.0 %f xlo xhi\n0.0 %f ylo yhi\n0.0 %f zlo zhi\n\nMasses\n\n1 1\n2 1\n\nAtoms\n\n"%(natoms,nmol,box_x,box_y,box_z))
    atom_id=0
    mol_id=0
    for ix in range(nmol_side_x):
        for iy in range(nmol_side_y):
            for iz in range(nmol_side_z):
                mol_id+=1
                r1=array([ix*lattice_x,iy*lattice_y,(iz+1)*lattice_z])
                atom_id+=1
                fout.write("%d %d 1 %.15f %.15f %.15f\n"%(atom_id,mol_id,r1[0],r1[1],r1[2]))
                r2=r1+bond_length*array([1,1,0.5])/sqrt(1*1+1*1+0.5*0.5)
                atom_id+=1
                fout.write("%d %d 2 %.15f %.15f %.15f\n"%(atom_id,mol_id,r2[0],r2[1],r2[2]))
    mol_id=0
    atom_id=0
    fout.write("\nBonds\n\n")    
    for ix in range(nmol_side_x):
        for iy in range(nmol_side_y):
            for iz in range(nmol_side_z):
                mol_id+=1
                atom_id+=1
                fout.write("%d 1 %d %d\n"%(mol_id,atom_id,atom_id+1))
                atom_id+=1
        
    



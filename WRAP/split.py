#!/usr/bin/env python	
import numpy as np
import os


##########################################################################################
#######Splitting POSCAR into header and XYZ part #########################################
#function takes in POSCAR and halves it into XYZ part and rest.
# write both files to the current location as HH and TAIL and Return handle for 
# lattiec vectors and XYZ

def SPLIT(F_name):
    IN = open(F_name,'r')
    out = open('HH', 'w')
    for line in IN:
        if (line[0] == "D" or line[0] == "C" or line[0] == "c" or line[0] == "d"):
           out.write('CART\n')
           out.close()
           out = open('TAIL', 'w')
        else:
           out.write(line)
    out.close()
    IN.close()
    # getting handle for lattice vector and TAIL
    os.system("head -n5 HH | tail -n3  > LL")
    LAT =np.loadtxt('LL')
    os.system("awk '{print $1,$2,$3}' TAIL > TAIL_2") 
    os.system("mv TAIL_2 TAIL")
    UU = np.loadtxt('TAIL')
    os.system("rm -f LL TAIL")
    return (UU,LAT)


 

###########################################################################################
###########################################################################################


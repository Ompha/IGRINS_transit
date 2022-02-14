'''
Run full IGRINS pipeline; code shows places where parameters can be changed
'''

import make_cube
import numpy as np
import wavecal
import do_pca

#Input parameters for WASP-76
path='/Users/megan/Documents/Projects/GeminiTransitSurvey/WASP76/20211029/reduced/' #path to reduced data
date='20211029' #date of observations
Tprimary_UT='2021-10-30T04:20:00.000' #time of primary transit midpoint for this epoch
Per=1.809886 #period
radeg=26.6329167 #RA of target in degrees
decdeg=2.7003889 #Dec of target in degrees
skyorder=1 #1 if sky frame was taken first in the night, 2 if sky frame was taken second
badorders=np.array([0, 1, 20, 21, 22, 23, 24, 25, 26, 27, 50, 51, 52, 53]) #set which orders will get ignored. Lower numbers are at the red end of the spectrum, and IGRINS has 54 orders
trimedges=np.array([100,-100]) #set how many points will get trimmed off the edges of each order: fist number is blue edge, second number is red edge
Vsys=-1.109 #Known systemic velocity from GAIA DR2 (can be found on exoplanet archive under the heading gamma (km/s))

#Make data cube and calculate barycentric velocity
phi,Vbary,grid_RAW,data_RAW,wlgrid,data=make_cube.make_cube(path,date,Tprimary_UT,Per,radeg,decdeg,skyorder,badorders,trimedges,plot=True,output=False,testorders=False)

#Perform wavelength calibration
wlgrid,wavecorrect=wavecal.correct(wlgrid,data,skyorder,plot=True,output=False)

#Perform PCA
wlgrid,pca_clean_data,pca_noplanet=do_pca.do_pca(wlgrid,wavecorrect,3,test_pca=False,plot=True,output=False)



import sys, os, math
import numpy as np
from matplotlib import pyplot as plt
from astropy.io import fits


nsa_agc_file='nsa_v0_1_2_with_AGC.Virgo.fits'
nsa_agc=fits.getdata(nsa_agc_file)

#hd_nsa_agc=fits.open(nsa_agc_file)
#print hd_nsa_agc[1].columns

nsa_wise_file= 'nsa_v0_1_2_wise.Virgo.fits'
nsa_wise=fits.getdata(nsa_wise_file)
#hd_nsa_wise=fits.open(nsa_wise_file)
#print hd_nsa_wise[1].columns

full_file='nsa_v1_2_fsps_v2.4_miles_chab_charlot_sfhgrid01.Virgo.fits'
full_data=fits.getdata(full_file)
full_data_hd=fits.open(full_file)
print full_data_hd[1].columns
#print full_data.Z, len(full_data.Z)
#print nsa_agc.ZDIST, len(nsa_agc.ZDIST)



'''
plt.figure()
t=plt.hist(nsa_agc.ZDIST*3.e5)
plt.show()
'''

plt.figure(figsize=(6,6))
#plt.scatter(full_data.RA,full_data.DEC,c=full_data.Z*3.e5,s=40,vmin=1000,vmax=3000)
plt.scatter(full_data.RA,full_data.DEC,c=full_data.MSTAR,s=40,vmin=6.,vmax=11.5)
plt.axis([150,220,-10,50])
plt.gca().invert_xaxis()
#plt.colorbar(fraction=.08,label='Recession Velocity')
plt.colorbar(fraction=.08,label='Log Stellar Mass')
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('ALL Sources in the Vicinity of Virgo')
plt.savefig('Virgo_ALL_sources.png')

vflag = nsa_agc.IALFALFA > -1
plt.figure(figsize=(6,6))
plt.scatter(full_data.RA[vflag],full_data.DEC[vflag],c=full_data.Z[vflag]*3.e5,s=40,vmin=1000,vmax=3000)
plt.axis([150,220,-10,50])
plt.gca().invert_xaxis()
plt.colorbar(fraction=.08,label='Recession Velocity')
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('ALFALFA HI Sources in the Vicinity of Virgo')
plt.savefig('Virgo_HI_sources.png')

vflag = (nsa_wise.W3MPRO > 0.) & (nsa_wise.W3SNR > 2.)  #22microns
#(nsa_wise.W3MPRO > 0.) & (nsa_wise.W3SNR > 2.)   # 12microns
plt.figure(figsize=(6,6))
plt.scatter(full_data.RA[vflag],full_data.DEC[vflag],c=full_data.Z[vflag]*3.e5,s=40,vmin=1000,vmax=3000)
plt.axis([150,220,-10,50])
plt.gca().invert_xaxis()
plt.colorbar(fraction=.08,label='Recession Velocity')
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('WISE Sources in the Vicinity of Virgo')
plt.savefig('Virgo_WISE_sources.png')



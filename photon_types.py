#!/usr/bin/env python
from myimports import * 
#***************************************************************************
import umass as umass 			#import components of UMass LXe Setup 
import photon_types as pht 		#import photon creation types 
import propagate_single as prop
import plot as plot
import datetime
from itertools import izip


# photon bomb, isotropic from position center
def photon_bomb(n,wavelength,pos):
    pos = np.tile(pos,(n,1))
    dir = uniform_sphere(n)
    
    pol = np.cross(dir,uniform_sphere(n))
    wavelengths = np.repeat(wavelength,n)
    return Photons(pos,dir,pol,wavelengths)


'''
def photon_bomb(n, wavelength, pos, direc):
    # Generate a series of photons which are scalar multiples of an initial direction vector; its like a photon gun that shoots photons along a line like a gun fires bullets. Should work well.
     #type: (object, object, object) -> object
    pos = np.tile(pos, (n, 1))
    scalars = np.linspace(0,  n, 0)
    indices = range(0, n + 1)
    
    for item, c, index in izip(pos, scalars, indices):
        item = item 
        pos[index] = item*c 
    dir = np.tile(direc, (n, 1))
    wavelengths = np.repeat(wavelength, n)
    return Photons(pos, dir, dir, wavelengths)



def photon_area_bomb(n, diameter, wavelength, x, y, z):
    radii = np.random.uniform(0, diameter / 2, n)
    angles = np.random.uniform(0, 2 * np.pi, n)
    points = np.empty((n, 3))
    points[:, 0] = np.sqrt(diameter / 2) * np.sqrt(radii) * np.cos(angles) + x
    points[:, 1] = np.repeat(y, n)
    points[:, 2] = np.sqrt(diameter / 2) * np.sqrt(radii) * np.sin(angles) + z
    pos = points
    # print "Ten Points of Photon Start Positions"
    print points[:10]
    dir = uniform_sphere(n)
    pol = np.cross(dir, uniform_sphere(n))
    wavelengths = np.repeat(wavelength, n)
    return Photons(pos, dir, pol, wavelengths)
'''

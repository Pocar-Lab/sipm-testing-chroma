#!/usr/bin/env python
from chroma.geometry import Material, Solid, Surface
import numpy as np
from myimports import *
import chroma, glob, pickle, yaml, sys, os
import matplotlib.pyplot as plt 
import pandas as pd


#***************************************************************************
#Surface properties for the SiPM 
fulldetect = Surface('fulldetect')			# detects everything that hits it
#fulldetect.Absorption = 1.0  
#fulldetect.fuSpecReflect = 0.3
#fulldetect.fuDiffuseReflect= 0.15
#fulldetect.set('absorb', fulldetect.fuAbsorption)
#fulldetect.set('reflect_diffuse',fulldetect.fuDiffuseReflect)
#fulldetect.set('reflect_specular',fulldetect.fuSpecReflect)
#

#***************************************************************************
# Functions needed for SiPM Reflection

def SetSurface(fulldetect, Name): 
		if Name == 'None':
			return None 
		else: 	
			SurfaceKeys1 = {'Transmission': 'transmissive', 'Thickness':'thickness', 'SurfaceModel':'model'}
			SurfaceKeys2 = {'Detection':'detect', \
				'Absorption':'absorb', \
				'DiffuseReflectivity':'reflect_diffuse', \
				'SpecularReflectivity':'reflect_specular', \
				'Reemission':'reemit', \
				'IndexOfRefractionRe':'eta', \
				'IndexOfRefractionIm':'k'}
			Surf = chroma.geometry.Surface(Name)
			Surf.name = Name
			for x in fulldetect.Surfaces.keys(): 
				if x in SurfaceKeys1.keys(): 
					if x == 'Transmission': 
						Surf.transmissive = self.OpticalParameters[Name][x]
					elif x == 'Thickness': 
						Surf.thickness = self.OpticalParameters[Name][x]
					elif x == 'SurfaceModel': 
						Surf.model = fulldetect.OpticalParameters[Name][x]
						if Surf.model == 3:
							Surf = fulldetect.ApplyReflectivityData(Surf)
				elif x in SurfaceKeys2.keys(): 
					if x in ['IndexOfRefractionRe', 'IndexOfRefractionIm']: 
						if all(y in self.OpticalParameters[Name].keys() for y in ['IndexOfRefractionRe', 'IndexOfRefractionIm']): 
							Surf.set(SurfaceKeys2[x], self.OpticalParameters[Name][x])
						else:
							continue 
					else: 
						Surf.set(SurfaceKeys2[x], self.OpticalParameters[Name][x])
			# print(', '.join('%s: %s' % item for item in vars(Surf).items()))
			return fulldetect

def Interpolate(Data):
	Angles = np.array(Data['AOI'])
	Reflectivity = np.array(Data['Reflectivity'])
	Transmittance = np.array(Data['Transmittance'])
	AnglesInterpolate = np.linspace(0, 90, 90)
	Reflectivity = np.interp(AnglesInterpolate, Angles, Reflectivity)
	Transmittance = np.interp(AnglesInterpolate, Angles, Transmittance)
	return AnglesInterpolate/180.0*np.pi, Reflectivity, Transmittance

def ApplyReflectivityData(fulldetect):
	Data = pd.read_csv('~/Desktop/github-chroma/sipm-testing-chroma-master/VUV4/ReflectivityTransmittance_vs_AOI_VUV4_UA.csv')
	Angles, Refl, Transm = Interpolate(Data)

	Reflection = []
	Transmission = []
	for ii,angle in enumerate(Angles): 
		reflect = np.tile(Refl[ii], len(chroma.geometry.standard_wavelengths))
		reflect = np.array(list(zip(chroma.geometry.standard_wavelengths, reflect)), dtype=np.float32)
		Reflection.append(reflect)
		transmit = np.tile(Transm[ii], len(chroma.geometry.standard_wavelengths))
		transmit = np.array(list(zip(chroma.geometry.standard_wavelengths, transmit)), dtype=np.float32)
		Transmission.append(transmit)
	angledep = chroma.geometry.DichroicProps(Angles, Reflection, Transmission)		
	Surface.dichroic_props = angledep
	return fulldetect

fulldetect = ApplyReflectivityData(fulldetect)
#fulldetect.set('detect', 1)
sipmsurface = Surface('sipmsurface')
sipmsurface.set('detect', 1)
#***************************************************************************
CuSurface = Surface('CuSurface')			# tailored to the real parameters of copper at this temperature/wavelength light
CuSurface.cuAbsorption = 0.95  #the most likely value is 35.8% ref for copper. Source:  #cu absorp-0.95
CuSurface.cuSpecReflect =0.05 #refractiveindex.info/?shelf=main&book=Cu&page=Werner #originally 0.5, CuSurface.cuSpecReflect = rp.CuSpecRef #0.05
CuSurface.cuDiffuseReflect= 0
CuSurface.set('eta', 0.97333)
CuSurface.set('k', 1.4735)
CuSurface.set('absorb', CuSurface.cuAbsorption)
CuSurface.set('reflect_diffuse', CuSurface.cuDiffuseReflect)
CuSurface.set('reflect_specular',CuSurface.cuSpecReflect)
#***************************************************************************
steelSurface = Surface('steelSurface')			# makes a fully absorbing surface
steelSurface.steelAbsorption = 1.0 #1.0
steelSurface.set('absorb', steelSurface.steelAbsorption)
steelSurface.set('reflect_diffuse', 0)
steelSurface.set('reflect_specular', 0.00)
#***************************************************************************
nothing = Surface('nothing')				# exactly what it says. Doesn't do anything.
nothing.set('detect', 0)
nothing.set('absorb', 0)
nothing.set('reflect_diffuse', 0)
nothing.set('reflect_specular', 0)
nothing.set('reemit', 0)
nothing.set('reemission_prob', 0)
nothing.transmissive = 1
nothing.model = 1

#***************************************************************************
quartzSurface = Surface('quartzSurface')  
quartzSurface.set('absorb', 1.0) #1
quartzSurface.set('detect', 0)
quartzSurface.set('reflect_specular', 0)
quartzSurface.set('reflect_diffuse', 0)
quartzSurface.transmissive = 1


#***************************************************************************

#ADDING SILICA INFO

silicaSurface = Surface('silicaSurface')			
#silicaSurface.set('absorb', 0.5)
silicaSurface.set('reflect_diffuse', 0)
silicaSurface.set('reflect_specular', 0.0) #0.2
#silicaSurface.set('reemit', 0)
silicaSurface.silicaEta = 1.69  
silicaSurface.set('eta', silicaSurface.silicaEta) #Real value of therefractive index of the surface
silicaSurface.transmissive = 1


silicaSurface.model = 1 #Model = complex, discovered from geometry_types.h. Allows photons to pass through surfaces based on the refractive index of the material
#Default model does not allow photons to pass through surfaces.

#****************************************************************
#Not used in code anymore, we use the SiPM as the detector -Seth 
pmtSurface = Surface('pmtSurface')
pmtSurface.set('reflect_diffuse', 0)
pmtSurface.set('reflect_specular', .60)
'''
pmtSurface.set('eta', 0.682)
pmtSurface.set('k', 2.45)
pmtSurface.model = 1
'''
pmtSurface.set('absorb', 0.25)
pmtSurface.set('detect', 0.15)
#****************************************************************
#Magic Copper
MagicCuSurface = Surface('MagicCuSurface')			# tailored to the real parameters of copper at this temperature/wavelength light
MagicCuSurface.set('absorb', 0.4) #0.4
MagicCuSurface.set('reflect_diffuse', 0.3)#0.3
MagicCuSurface.set('reflect_specular', 0.3) #0.3
#****************************************************************

AlSurface = Surface('AlSurface')			# tailored to the real parameters of copper at this temperature/wavelength light
AlSurface.AlAbsorption = 0.1 #0.1
AlSurface.AlSpecReflect = 0.9 #0.9
AlSurface.AlDiffuseReflect= 0 #AlSurface.AlDiffuseReflect= rp.AlDiffRef #0 for now
AlSurface.set('absorb', AlSurface.AlAbsorption)
AlSurface.set('reflect_diffuse', AlSurface.AlDiffuseReflect) #originally 0.5
AlSurface.set('reflect_specular',AlSurface.AlSpecReflect)

#***************************************************
#adding source 
AM_241Surface = Surface('AM_241Surface')			
#silicaSurface.set('absorb', 1.0)
AM_241Surface.set('reflect_diffuse', 0)
AM_241Surface.set('reflect_specular', 0)
#silicaSurface.set('reemit', 0)
AM_241Surface.AM_241Eta = 1.61 
AM_241Surface.set('eta', AM_241Surface.AM_241Eta) #Real value of therefractive index of the surface
AM_241Surface.transmissive = 1

AM_241Surface.model = 1 #Model = complex, discovered from geometry_types.h. Allows photons to pass through surfaces based on the refractive index of the material
#Default model does not allow photons to pass through surfaces

#***************************************************

#Teflon Reflector
TefSurface = Surface('TefSurface')
TefSurface.TefAbsorption = 0.0     #real value very close to 0 (less than 0.1) 
TefSurface.TefSpecReflect = 0.05 #value from nExo wiki, originally 0.05,
TefSurface.TefDiffuseReflect=0.95
TefSurface.set('eta', 1.36)
#TefSurface.set('k', -)
TefSurface.set('reflect_diffuse', TefSurface.TefDiffuseReflect) #values from nExo materials, originally 0.95, 
TefSurface.set('reflect_specular',TefSurface.TefSpecReflect)
TefSurface.set('absorb', TefSurface.TefAbsorption)
#TefSurface.set('detect', 1.0)

#***************************************************





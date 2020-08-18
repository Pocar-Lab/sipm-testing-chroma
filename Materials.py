#!/usr/bin/env python
from chroma.geometry import Material, Solid, Surface
import numpy as np
#***************************************************************************
#***************************************************************************
sipm = Material('sipm')
sipm.set('detection', 1)

copper = Material('copper')
copper.set('refractive_index', 0.97333) # 0.87 #https://refractiveindex.info/?shelf=main&book=Cu&page=Werner with wavelength 175nm extrapolated on TREND function excel
copper.set('absorption_length',50) #1058100 
copper.set('scattering_length',1e6) #10e6
copper.density = 8.96
copper.composition = {'Cu' : 1.00}
#***************************************************************************
#***************************************************************************
vacuum = Material('vac')
vacuum.set('refractive_index', 1.0)
vacuum.set('absorption_length', 0)
vacuum.set('scattering_length', 1e6)
vacuum.set('reemission_prob', 0)
#***************************************************************************
#***************************************************************************
LXenon = Material('LXenon')
LXenon.set('refractive_index', 1.69) #https://arxiv.org/ftp/physics/papers/0307/0307044.pdf #possibly 1.57 but lower occurances #1.69
LXenon.set('absorption_length', 1e6) #20000 Changed 364 --> 0 8/9/2018, used 1000mm June 11 2019
LXenon.set('scattering_length', 350) #https://arxiv.org/pdf/physics/0407033.pdf #Alabama uses 350, nEXO_MC 400 #study shows no difference in our set up, changed to 400mm June 11 2019
LXenon.density = 2.942 #2.942

#***************************************************************************
quartz = Material('quartz') #material inside the angle dependant surface of sipm 
quartz.set('refractive_index', 1.69) #0
quartz.set('absorption_length', 100)
quartz.set('scattering_length', 100)

#***************************************************************************
fullAbsorb = Material('fullAbsorb')
fullAbsorb.set('absorb', 1)
fullAbsorb.set('refractive_index', 1) #0
fullAbsorb.set('absorption_length', 0.00000000001)
fullAbsorb.set('scattering_length', 0.00000000001)
fullAbsorb.density = 1
#***************************************************************************
#***************************************************************************
steel = Material('steel')
steel.set('absorb', 1)
steel.set('refractive_index', 0) #0
steel.set('absorption_length', 0)
steel.set('scattering_length', 1e6)
steel.density = 8.05 #8.05

#***************************************************************************
#***************************************************************************
silicon = Material('silicon')
silicon.set('refractive_index', 1.05) #3.33
silicon.set('absorption_length', 100) #Nexo's, very debatable #364
silicon.set('scattering_length', 100) #Nexo's, very debatable #400
silicon.density = 2.329 #2.329
#***************************************************************************

#Test import, the values could be wrong.  more invistgation must be done!
silica = Material('silica')
silica.set('refractive_index', 1.58)       # http://www.rit.edu/kgcoe/microsystems/lithography/thinfilms/cgi-bin/database.cgi?sio2_3_vuv.csv #1.61 #was 1.8 I changed it back to 1.61
silica.set('absorption_length', 100)       #10cm the value from nEXO_MC #100
silica.set('scattering_length', 350)       #no known real value
silica.density = 2.2                        #real value is 2.20
silica.composition = {'silica' : 1.00}


#*********************************************************
#*********************************************************
Magiccopper = Material('Magiccopper')
Magiccopper.set('refractive_index', 1.3)             #1.3
Magiccopper.set('absorption_length', 10000)          #10000 from 0 8/9/18
Magiccopper.set('scattering_length',1e6)
Magiccopper.density = 8.96
Magiccopper.composition = {'Cu' : 1.00}
#*********************************************************
#*********************************************************
Al = Material('Al')
Al.set('refractive_index', 0.089) #info can be found "McPeal et al. 2015. lambda:175nm or 0.175 um. Website: https://refractiveindex.info/?shelf=3d&book=metals&page=aluminium #0.089
Al.set('absorption_length', 10000) #10000 from 0 8/9/18 #1340700
Al.set('scattering_length',1e6)
Al.density = 2.710 #2.710
Al.composition = {'Al' : 1.00}
#*********************************************

teflon = Material('teflon') #this material is what the reflector is made of 
teflon.set('refractive_index', 1.36)    #1.356 rounded off to 1.36. Data obtained from https://polymerdatabase.com/polymer%20physics/Ref%20Index%20Table%20.html #1.36
teflon.set('absorption_length', 100)  #unit:cm^-1, value obtained using the photon energy of silicon that correspond to table: https://physics.nist.gov/PhysRefData/XrayMassCoef/ComTab/teflon.html #73.5
teflon.set('scattering_length', 1e6)    #unit:cm, cannot find at the moment, will get data later 
teflon.density = 2.2                  #unit:g/cm^3, divide by 2??? Source: "X-Ray Attenuation and Absorption for Materials of Dosimetric Interest" by J.H Hubell and S.M Seltzer #2.2



#!/usr/bin/env python
from myimports import * 

Usetup = Detector(mat.LXenon) # filled the volume with whatever material is appropriate (in our case LXe)
#Usetup = Detector()



############################# test cell 27.5mm ########################
Usetup.distance = 0 


print ("  Creating Blank LXe Setup:	importing LXE cell		Done")
path = "/home/lab/Desktop/New_parts_38mm/" # file path to the STL files of the assembly (something created in SolidWorks)
path2 = "/home/lab/Desktop/LXe_cell_centered/" #the path to the corrected VUV4
path3 = "/home/lab/Desktop/Chroma/UMass_Chroma/UMass/New_Cell/" #the path to the corrected VUV4
path4 = "/home/chroma/Desktop/STL_Files/Tef38mm/" #the path to including teflon reflector in the simulation 
path5 = "/home/chroma/Desktop/STL_Files/Tef27mm/"  #the path to including teflon reflector in the simulation 


grey =0x3365737e
dark_orange =0x33a67c00
blue = 0x33ffbf00  #its orange :P
green = 0xff00
blue2 = 0x0000ff
red = 0xFF0000
yellow = 0xffff00


#distance = 15 # the change in separation between source and detector (in mm). 0 => 13 mm separation between source and detector. It also means 2mm separation between the two copper plates. (new change in separation between source and detector is 0=>38mm respectively with the 38m  diamter teflon reflector washer between the two) 

#***************************************************************************
'''
#### Copper plates around source and VUV4 #####

#updated code for including teflon reflector 
a = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - APD Disk_wdrill_1-1.STL") # First two (a & b) are the copper holders for the detectors 
aS = Solid(a, mat.copper, mat.LXenon, surf.MagicCuSurface, blue) #Solid(mesh, material of mesh, material surrounding mesh, surface of mesh, color)
Usetup.add_solid(aS, displacement=(0, Usetup.distance,0))

#b is the top copper ring. remove it and you will see the sipm

b = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - APD Disk_wdrill_1-2.STL")
bS = Solid(b, mat.copper, mat.LXenon, surf.MagicCuSurface,blue)
Usetup.add_solid(bS, displacement=(0,0,0))

#  end  ######

#***************************************************************************

#### Al filler ####

#new code (with 38 mm diamater teflon reflector- current reflector in use)

c = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - Al_filler-1.STL") # Aluminum volume filler. Also negligible in effect.
cS = Solid(c, mat.Al, mat.LXenon, surf.AlSurface, green)
Usetup.add_solid(cS, displacement=(0,0,0))


#***************************************************************************
'''
#### Insert VUV4 parts  fulldetect ####

#updated code with the 38mm teflon reflector 

e = mesh_from_stl(path4+"thin_sipm.stl") # module #This is the photosensor area in our detector (6*6mm)
eS = Solid(e, mat.silicon, mat.quartz, data.bottom(e, surf.sipm, surf.fullAbsorb), data.bottom(e, red, blue2)) #mat internal => usually silicon
# eS = Solid(e, mat.silicon, mat.LXenon, surf.sipm, blue2)
Usetup.add_pmt(eS, displacement=(0,0,0)) #this was displacement=(0,-0.5,0)

# Reflective surface over (or encasing) the SiPM
refsurf = mesh_from_stl(path4+"sipm_quartz.stl")
refsurfS = Solid(refsurf, mat.quartz, mat.LXenon, data.bottom(refsurf, surf.reflective, surf.fullAbsorb), yellow)
Usetup.add_solid(refsurfS, displacement=(0,0,0))

'''
k = mesh_from_stl(path4+ "20190619_cell_with_reflector_38mm - Assem2-2 Pho S5-2.STL") # The base (something we do not need to worry about) \
kS = Solid(k, mat.steel, mat.LXenon, surf.steelSurface, blue)
Usetup.add_solid(kS, displacement=(0,0,0))


x = mesh_from_stl(path4+ "20190619_cell_with_reflector_38mm - Assem2-2 Cu Holder-1.STL") # The base (something we do not need to worry about)
xS = Solid(x, mat.steel, mat.LXenon, surf.steelSurface, blue)
Usetup.add_solid(xS, displacement=(0,0,0))

######  end  ######

#***************************************************************************

#### Teflon Reflector #### 
w = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - teflon_reflector-1.STL") #This is the 38mm reflector that is currently in the real model in the 
wS = Solid(w, mat.teflon, mat.LXenon, surf.TefSurface, green ) #defined teflon(materials),defined teflon surface (surface)
Usetup.add_solid(wS, displacement=(0,0,0))

######  end  ######

#***************************************************************************

#### Source layers   Usetup.distance #####

#updated code to support teflon reflector
o = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - Am-241-1 source_Am-241_part1-1.STL")#,20190604_test_cell_w_maxreflector_fix - Am-241-4 source_Am-241_part1-1.STL
oS = Solid(o, mat.steel, mat.LXenon, surf.steelSurface, green )
Usetup.add_solid(oS, displacement=(0,0,0))

p = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - Am-241-1 source_Am-241_part2-1.STL")#,20190604_test_cell_w_maxreflector_fix - Am-241-4 source_Am-241_part2-1.STL
pS = Solid(p, mat.steel, mat.LXenon, surf.steelSurface, green)
Usetup.add_solid(pS, displacement=(0,0,0))
'''

q = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - Am-241-1 source_Am-241_part3-1.STL") 
qS = Solid(q, mat.steel, mat.vacuum, surf.steelSurface, red)
# Usetup.add_solid(qS, displacement=(0,0,0))
'''
m = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - Am-241-1 Am-241_holder-2.STL")
mS = Solid(m, mat.steel, mat.vacuum, surf.steelSurface, green)
Usetup.add_solid(mS, displacement=(0,0,0))





######  end  ######

#***************************************************************************

#### The 4 screws in the cell ####


#updated code for inclusion of the 38mm in diameter teflon reflector washer (threadedrod_3)

s = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - threadedrod_4-1.STL") # These final two (s & t) are the threaded rods supporting the assembly. Negligible contribution.
sS = Solid(s, mat.steel, mat.LXenon, surf.steelSurface, green)
Usetup.add_solid(sS, displacement=(0,0,0))


t = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - threadedrod_4-3.STL")
tS = Solid(t, mat.steel, mat.LXenon, surf.steelSurface, green)
Usetup.add_solid(tS, displacement=(0,0,0))

v = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - threadedrod_4-4.STL") # These final two (s & t) are the threaded rods supporting the assembly. Negligible contribution.
vS = Solid(v, mat.steel, mat.LXenon, surf.steelSurface, green)
Usetup.add_solid(vS, displacement=(0,0,0))

r = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - threadedrod_4-5.STL")
rS = Solid(r, mat.steel, mat.LXenon, surf.steelSurface, green)
Usetup.add_solid(rS, displacement=(0,0,0))




######  end  ######

#***************************************************************************

#### Fused Silica Window ####


#updated code (with reflector included) 

#Copper ring top
#the gasket should be offset from the cu plates holding the source by 2.25 mm (it is the nut's thicknesses. 23.25 is 0 for the holders
d = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - silica_window-1 silica_gasket-1.STL")
dS = Solid(d, mat.copper, mat.LXenon, surf.CuSurface, blue)
Usetup.add_solid(dS, displacement=(0,0,0))


#Copper ring bottom  MagicCuSurface

f = mesh_from_stl(path4+"20190619_cell_with_reflector_38mm - silica_window-1 silica_gasket-2.STL")
fS = Solid(f, mat.copper, mat.LXenon, surf.CuSurface, blue)

Usetup.add_solid(fS, displacement=(0,0,0))


#Silica window (fused silica)

z = mesh_from_stl(path5+"20190619_cell_with_reflector_27mm - VPW42-Solidworks-2.STL")
zS = Solid(z, mat.silica, mat.LXenon, surf.silicaSurface, red)

Usetup.add_solid(zS, displacement=(0,0,0))
'''
###### end #######

#***************************************************************************


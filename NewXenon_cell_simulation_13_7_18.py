
#!/usr/bin/env python
from myimports import *
#from matplotlib import colors
from array import array
import pylab
import pickle
#import pandas as pd ##

start_begin = time.time() 
print 
print ("=====================================================================")
arg_list = arg.main(sys.argv[1:])
print ("=====================================================================")
print ("  Start Simulation				Done")
print ("=====================================================================")
#***************************************************************************

#***************************************************************************
import umass as umass 			#import components of UMass LXe Setup 
import photon_types as pht 		#import photon creation types 
import propagate_single as prop
import plot as plot
import Surfaces as Surfaces

import datetime
from matplotlib import colors 
from matplotlib.offsetbox import AnchoredText #Allows the usage of textboxes
###########################################################################
bulk = 0
SurfaceAbs = 0
RayleighSct = 0
ReflectDif = 0
SpecularRef = 0
noSeen = 0
mean_photons_Seen = 0
#***************************************************************************
print ("=====================================================================")
print ("  Mesh Imports					Successful")
print ("=====================================================================")
#***************************************************************************
umass.Usetup.flatten()
#if(arg_list[2]): # taking the terminal directive '-v' to view the assembly (via pygame) before simulating
	#view (umass.Usetup)
umass.Usetup.bvh = load_bvh(umass.Usetup)		# Take these lines as standard syntax for importing a geometry from STL into the simulation
sim = Simulation(umass.Usetup, seed=arg_list[5], geant4_processes=0)  #This is where you can add/remove seeding. To remove seeding just delete seed=1
#***************************************************************************
numPhotons = arg_list[0] #Number of photons used for the statistics and for the SiPM distribution plot
numPhotons2 = 1500 #Number of photons used for the photon track plot #1500
numPhotons3 = 20000 #Numberof photons used for the distribution in cell plot #5000


"====================initializing root components======================"
runs = 1
# How many times should the simulation run?
photon_nr = array('d', [0])
"====================start step by steps simulation===================="
nr_hits = np.zeros((runs)) # need to define the array as the right size to fit all the runs of the simulation
doRandom = prop.getRandom() #random direction components for photons


point_zero = data.get_center(umass.q)

#xyz coord of the point source
point_zero[0] = point_zero[0]
point_zero[1] = point_zero[1]
point_zero[2] = point_zero[2] 

q_center = data.get_center(umass.q)
v_center = umass.q.get_triangle_centers()

v_center[0] = v_center[0] 
v_center[1] = v_center[1] 
v_center[2] = v_center[2] 

messung_dir = []   #messung means measurement in German 
vertex = []
vertex2 = []
'''
b=0.05 #step size of copper diffuse and spec reflection 
c=0.1  #step size of aluminum diffuse and absorption 

#text_file = open(Teflon38mm.txt, 'w')

while Surfaces.TefSurface.TefDiffuseReflect<=1.00 and Surfaces.TefSurface.TefDiffuseReflect>=0.85 and Surfaces.TefSurface.TefSpecReflect<=0.15 and Surfaces.TefSurface.TefSpecReflect>=0.0:
	if float(Surfaces.TefSurface.TefDiffuseReflect) + float(Surfaces.TefSurface.TefSpecReflect) == 1.0:
		Surfaces.TefSurface.TefDiffuseReflect+=float(0.05)
		Surfaces.TefSurface.TefSpecReflect+=float(-0.05)
	else:
		break 
	Surfaces.CuSurface.cuDiffuseReflect=0
	Surfaces.CuSurface.cuSpecReflect=0
	Surfaces.CuSurface.cuAbsorption=1

	for j in range(3):
		if Surfaces.CuSurface.cuAbsorption!=1.0:
			Surfaces.CuSurface.cuDiffuseReflect+=float(b)
			Surfaces.CuSurface.cuSpecReflect+=float(-b) 
			Surfaces.AlSurface.AlAbsorption=0.0
			Surfaces.AlSurface.AlSpecReflect=1.0
			for k in range(3):
				Surfaces.AlSurface.AlAbsorption+=float(c)
				Surfaces.AlSurface.AlSpecReflect+=float(-c)
				bulk = 0

				SurfaceAbs=0
				RayleighSct = 0
				ReflectDif = 0
				SpecularRef = 0
				noSeen = 0
				mean_photons_Seen = 0
				for i in range(runs):
	
					photonbomb = pht.photon_bomb(numPhotons,175,(point_zero[0], point_zero[1] , point_zero[2]))
					photonbomb2 = pht.photon_bomb(numPhotons2,175,(point_zero[0], point_zero[1] , point_zero[2])) 
					photonbomb3 = pht.photon_bomb(numPhotons3,175,(point_zero[0], point_zero[1] , point_zero[2])) #Used 3 different bombs, one for each graph to avoid issues with vertex array
					photons, photon_track = prop.propagate_photon(photonbomb, numPhotons, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])
					photons2, photon_track2 = prop.propagate_photon(photonbomb2, numPhotons2, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])
					photons3, photon_track3 = prop.propagate_photon(photonbomb3, numPhotons3, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])

#Flagging the different type of photons in the simulaton and adding each type of them into an array
					no = (photons.flags & (0x1 << 0)).astype(bool)
					detected = (photons.flags & (0x1 << 2)).astype(bool)
					absorbB  = (photons.flags & (0x1 << 1)).astype(bool)
					absorbS  = (photons.flags & (0x1 << 3)).astype(bool)
					RayleighScattering = (photons.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion  = (photons.flags & (0x1 << 5)).astype(bool)
					SpecularReflection = (photons.flags & (0x1 << 6)).astype(bool)
					nr_hits[i] = len(photons.pos[detected])
					mean_photons_Seen += nr_hits[i]
					bulk += len(photons.pos[absorbB]) # this is another example of a type of event you can look for (bulk absorbtion). you'd then have to average over all the runs.
					SurfaceAbs += len(photons.pos[absorbS])
					RayleighSct += len(photons.pos[RayleighScattering])
					ReflectDif += len(photons.pos[ReflectDiffusion])
					noSeen += len(photons.pos[no])
					SpecularRef += len(photons.pos[SpecularReflection])
					photon_nr[0] = (nr_hits[i]*1/numPhotons)
					messung_dir.append(photons.dir[detected])
					vertex.append(photons.pos[detected])
	
					no2 = (photons2.flags & (0x1 << 0)).astype(bool)
					detected2 = (photons2.flags & (0x1 << 2)).astype(bool)
					absorbB2  = (photons2.flags & (0x1 << 1)).astype(bool)
					absorbS2  = (photons2.flags & (0x1 << 3)).astype(bool)
					RayleighScattering2 = (photons2.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion2  = (photons2.flags & (0x1 << 5)).astype(bool)
					SpecularReflection2 = (photons2.flags & (0x1 << 6)).astype(bool)
					vertex2.append(photons2.pos[detected2])
					no3 = (photons3.flags & (0x1 << 0)).astype(bool)
					detected3 = (photons3.flags & (0x1 << 2)).astype(bool)
					absorbB3  = (photons3.flags & (0x1 << 1)).astype(bool)
					absorbS3  = (photons3.flags & (0x1 << 3)).astype(bool)
					RayleighScattering3 = (photons3.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion3  = (photons3.flags & (0x1 << 5)).astype(bool)
					SpecularReflection3 = (photons3.flags & (0x1 << 6)).astype(bool)
				
	



				total_photons_seen = mean_photons_Seen
				mean_photons_Seen /= runs
				bulk /= runs
				SurfaceAbs /= runs
				RayleighSct /= runs
				ReflectDif /= runs
				SpecularRef /= runs
				noSeen /= runs
				detectionEfficiency = (total_photons_seen/(numPhotons*runs))
				std = np.sqrt(total_photons_seen)
				detectionEfficiencyStd = (std/(numPhotons*runs))

				print detectionEfficiency, round(detectionEfficiencyStd, 6), Surfaces.TefSurface.TefDiffuseReflect, Surfaces.TefSurface.TefSpecReflect, Surfaces.TefSurface.TefAbsorption, Surfaces.CuSurface.cuAbsorption, Surfaces.CuSurface.cuSpecReflect, Surfaces.CuSurface.cuDiffuseReflect, Surfaces.AlSurface.AlAbsorption, Surfaces.AlSurface.AlSpecReflect, Surfaces.AlSurface.AlDiffuseReflect
				#HELP ME PLZ code: text_file.writelines(L) for L= [detectionEfficiency, round(detectionEfficiencyStd, 6), TefDiffRef, TefSpecRef, TefAbsorb, CuAbsorb, CuSpecRef, CuDiffRef, AlAbsorb, AlSpecRef, AlAbsorb]
			
		if Surfaces.CuSurface.cuDiffuseReflect==0 and Surfaces.CuSurface.cuSpecReflect==0:
			Surfaces.CuSurface.cuAbsorption=1.0


			Surfaces.AlSurface.AlAbsorption=0.0
			Surfaces.AlSurface.AlSpecReflect=1.0
			for k in range(3):
				Surfaces.AlSurface.AlAbsorption+=float(c)
				Surfaces.AlSurface.AlSpecReflect+=float(-c)
			
				bulk = 0
				SurfaceAbs=0
				RayleighSct = 0
				ReflectDif = 0
				SpecularRef = 0
				noSeen = 0
				mean_photons_Seen = 0
				for i in range(runs):
	
					photonbomb = pht.photon_bomb(numPhotons,175,(point_zero[0], point_zero[1] , point_zero[2]))
					photonbomb2 = pht.photon_bomb(numPhotons,175,(point_zero[0], point_zero[1] , point_zero[2])) #numphotons2
					photonbomb3 = pht.photon_bomb(numPhotons3,175,(point_zero[0], point_zero[1] , point_zero[2])) #Used 3 different bombs, one for each graph to avoid issues with vertex array
					photons, photon_track = prop.propagate_photon(photonbomb, numPhotons, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])
					photons2, photon_track2 = prop.propagate_photon(photonbomb2, numPhotons, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2]) #numphotons2
					photons3, photon_track3 = prop.propagate_photon(photonbomb3, numPhotons3, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])

#Flagging the different type of photons in the simulaton and adding each type of them into an array
					no = (photons.flags & (0x1 << 0)).astype(bool)
					detected = (photons.flags & (0x1 << 2)).astype(bool)
					absorbB  = (photons.flags & (0x1 << 1)).astype(bool)
					absorbS  = (photons.flags & (0x1 << 3)).astype(bool)
					RayleighScattering = (photons.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion  = (photons.flags & (0x1 << 5)).astype(bool)
					SpecularReflection = (photons.flags & (0x1 << 6)).astype(bool)
					nr_hits[i] = len(photons.pos[detected])
					mean_photons_Seen += nr_hits[i]
					bulk += len(photons.pos[absorbB]) # this is another example of a type of event you can look for (bulk absorbtion). you'd then have to average over all the runs.
					SurfaceAbs += len(photons.pos[absorbS])
					RayleighSct += len(photons.pos[RayleighScattering])
					ReflectDif += len(photons.pos[ReflectDiffusion])
					noSeen += len(photons.pos[no])
					SpecularRef += len(photons.pos[SpecularReflection])
					photon_nr[0] = (nr_hits[i]*1/numPhotons)
					messung_dir.append(photons.dir[detected])
					vertex.append(photons.pos[detected])
	
					no2 = (photons2.flags & (0x1 << 0)).astype(bool)
					detected2 = (photons2.flags & (0x1 << 2)).astype(bool)
					absorbB2  = (photons2.flags & (0x1 << 1)).astype(bool)
					absorbS2  = (photons2.flags & (0x1 << 3)).astype(bool)
					RayleighScattering2 = (photons2.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion2  = (photons2.flags & (0x1 << 5)).astype(bool)
					SpecularReflection2 = (photons2.flags & (0x1 << 6)).astype(bool)
					vertex2.append(photons2.pos[detected2])
					no3 = (photons3.flags & (0x1 << 0)).astype(bool)
					detected3 = (photons3.flags & (0x1 << 2)).astype(bool)
					absorbB3  = (photons3.flags & (0x1 << 1)).astype(bool)
					absorbS3  = (photons3.flags & (0x1 << 3)).astype(bool)
					RayleighScattering3 = (photons3.flags & (0x1 << 4)).astype(bool)
					ReflectDiffusion3  = (photons3.flags & (0x1 << 5)).astype(bool)
					SpecularReflection3 = (photons3.flags & (0x1 << 6)).astype(bool)
				
	



				total_photons_seen = mean_photons_Seen
				mean_photons_Seen /= runs
				bulk /= runs
				SurfaceAbs /= runs
				RayleighSct /= runs
				ReflectDif /= runs
				SpecularRef /= runs
				noSeen /= runs
				detectionEfficiency = (total_photons_seen/(numPhotons*runs))
				std = np.sqrt(total_photons_seen)
				detectionEfficiencyStd = (std/(numPhotons*runs))

				print detectionEfficiency, str(round(detectionEfficiencyStd, 6)), Surfaces.TefSurface.TefDiffuseReflect, Surfaces.TefSurface.TefSpecReflect,Surfaces.TefSurface.TefAbsorption, Surfaces.CuSurface.cuAbsorption, Surfaces.CuSurface.cuSpecReflect, Surfaces.CuSurface.cuDiffuseReflect, Surfaces.AlSurface.AlAbsorption, Surfaces.AlSurface.AlSpecReflect, Surfaces.AlSurface.AlDiffuseReflect, 'meow'
				#PLZZ :( code:text_file.writelines(L) for L= [detectionEfficiency, str(round(detectionEfficiencyStd, 6)), TefDiffRef, TefSpecRef,TefAbsorb, CuAbsorb, CuSpecRef, CuDiffRef, AlAbsorb, AlSpecRef, AlAbsorb]
			Surfaces.CuSurface.cuDiffuseReflect=-0.05
			Surfaces.CuSurface.cuSpecReflect=0.1
			Surfaces.CuSurface.cuAbsorption=0.95
#text_file.close()
'''
for i in range(runs):
	
	photonbomb = pht.photon_bomb(numPhotons,175,(point_zero[0], point_zero[1] , point_zero[2]))
	photonbomb2 = pht.photon_bomb(numPhotons2,175,(point_zero[0], point_zero[1] , point_zero[2])) #numPhotons2
	photonbomb3 = pht.photon_bomb(numPhotons3,175,(point_zero[0], point_zero[1] , point_zero[2])) #Used 3 different bombs, one for each graph to avoid issues with vertex array
	photons, photon_track = prop.propagate_photon(photonbomb, numPhotons, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])
	photons2, photon_track2 = prop.propagate_photon(photonbomb2, numPhotons2, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2]) #numPhotons2
	photons3, photon_track3 = prop.propagate_photon(photonbomb3, numPhotons3, 100, umass.Usetup, doRandom[0], doRandom[1], doRandom[2])
	
#Flagging the different type of photons in the simulaton and adding each type of them into an array
	no = (photons.flags & (0x1 << 0)).astype(bool)
	detected = (photons.flags & (0x1 << 2)).astype(bool)
	absorbB  = (photons.flags & (0x1 << 1)).astype(bool)
	absorbS  = (photons.flags & (0x1 << 3)).astype(bool)
	#RayleighScattering = (photons.flags & (0x1 << 4)).astype(bool)
	ReflectDiffusion  = (photons.flags & (0x1 << 5)).astype(bool)
	SpecularReflection = (photons.flags & (0x1 << 6)).astype(bool)
	nr_hits[i] = len(photons.pos[detected])
	mean_photons_Seen += nr_hits[i]
	bulk += len(photons.pos[absorbB]) # this is another example of a type of event you can look for (bulk absorbtion). you'd then have to average over all the runs.
	SurfaceAbs += len(photons.pos[absorbS])
	#RayleighSct += len(photons.pos[RayleighScattering])
	ReflectDif += len(photons.pos[ReflectDiffusion])
	noSeen += len(photons.pos[no])
	SpecularRef += len(photons.pos[SpecularReflection])
	photon_nr[0] = (nr_hits[i]*1/numPhotons)
	messung_dir.append(photons.dir[detected])
	vertex.append(photons.pos[detected])
	
	no2 = (photons2.flags & (0x1 << 0)).astype(bool)
	detected2 = (photons2.flags & (0x1 << 2)).astype(bool)
	absorbB2  = (photons2.flags & (0x1 << 1)).astype(bool)
	absorbS2  = (photons2.flags & (0x1 << 3)).astype(bool)
	#RayleighScattering2 = (photons2.flags & (0x1 << 4)).astype(bool)
	ReflectDiffusion2  = (photons2.flags & (0x1 << 5)).astype(bool)
	SpecularReflection2 = (photons2.flags & (0x1 << 6)).astype(bool)
	vertex2.append(photons2.pos[detected2])
	no3 = (photons3.flags & (0x1 << 0)).astype(bool)
	detected3 = (photons3.flags & (0x1 << 2)).astype(bool)
	absorbB3  = (photons3.flags & (0x1 << 1)).astype(bool)
	absorbS3  = (photons3.flags & (0x1 << 3)).astype(bool)
	RayleighScattering3 = (photons3.flags & (0x1 << 4)).astype(bool)
	ReflectDiffusion3  = (photons3.flags & (0x1 << 5)).astype(bool)
	SpecularReflection3 = (photons3.flags & (0x1 << 6)).astype(bool)
				
	


total_photons_seen = mean_photons_Seen
mean_photons_Seen /= runs
bulk /= runs
SurfaceAbs /= runs
RayleighSct /= runs
ReflectDif /= runs
SpecularRef /= runs
noSeen /= runs
detectionEfficiency = (total_photons_seen/(numPhotons*runs))
std = np.sqrt(total_photons_seen)
detectionEfficiencyStd = (std/(numPhotons*runs))

print (np.sqrt(std**2/total_photons_seen))
print ("Photons detected Per Run", nr_hits)
print ("Detected: 	", total_photons_seen, "+/-   ", str(round(std, 0)))
print ("Detection Efficiency:   ", str(round(detectionEfficiency, 7)), "+/-   ", str(round(detectionEfficiencyStd, 7)))	
print ("Bulk absorb:      ", bulk)
print ("Surface Absorption:   ",SurfaceAbs)
print ("RayleighScattering:    ",RayleighSct)
print ("ReflectDiffusion:     ", ReflectDif)
print ("Specular Reflect:    ", SpecularRef)
print ("No photons interacted:   ", noSeen)
# print ("Sum of detected+Bulk absorbed+surface absorbed+not interacted+ reflect diffusive = ", mean_photons_Seen+bulk+SurfaceAbs+noSeen+ReflectDif )


# finding the y location of the reflected photons to understand the geoy.
#ref1 = photons.pos[SpecularReflection]

#print ref1[:,1]
#

if(arg_list[3]):

	endPosRotated0 = photons.pos[detected]
	
	fig = plt.figure(figsize=(20, 15))
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(endPosRotated0[:,0], endPosRotated0[:,1], endPosRotated0[:,2], c='pink', label='Detected Photons = ' + str(total_photons_seen))
	#Outline of the VUV4
	#ax.plot((86.5, 92.5), (24.441, 24.441), 86, color='k', label='VUV4')
	#ax.plot((86.5, 92.5), (24.441, 24.441), 92, color='k')
	#ax.plot((86.5, 86.5), (24.441, 24.441), (86, 92), color='k')
	#ax.plot((92.5, 92.5), (24.441, 24.441), (86, 92), color='k')
	ax.set_xlabel('X Label (mm)')
	ax.set_ylabel('Y Label (mm)')
	ax.set_zlabel('Z Label (mm)')
	plt.title(ax.title, y=1.03)
	ax.set_title('Photon Distribution on SiPM' + '\n' + datetime.date.today().strftime('%B %d, %Y') + '\n' + 'Simulated Photons = ' + str(numPhotons*runs))
	ax.title.set_fontsize(25)
	ax.legend(loc='best' , fontsize = 18)
	textstr = '\n'.join(('Aluminum Filler: ' + str(surf.steelSurface.steelAbsorption*100) + '% absorbative', 'Fused Silica Window: Refractice Index = ' +str(surf.silicaSurface.silicaEta), 'Copper: '+str(surf.CuSurface.cuAbsorption*100)+'% absorb ' + str(surf.CuSurface.cuSpecReflect*100)+'% specular reflect'))
	ax.text2D(0, 0.93, textstr, fontsize=14, transform=ax.transAxes)
	plt.ylim(64.405, 65) #plt.ylim(35,60)
	
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
																																																																																																																																																																																																																																																																																					
	plt.show()
	

	
########################################### PHOTON EVENTS ###########################################




if(arg_list[3]):
	vertex2 = photons2.pos[detected2] 

	angles = []
	pos_p = []
	
	
	for i in range(runs):
		angles.append(data.incident_angle(messung_dir[i]))
		

	v_center = umass.e.get_triangle_centers() #e
	o_center = umass.q.get_triangle_centers()
	#plot.event_display(numPhotons, photon_track, vertex, o_center, v_center, point_zero) 
	fig = plt.figure(figsize=(30, 20))
	ax = fig.add_subplot(111, projection='3d')
	labelbool = False
	labelbool2 = False
	for i in range(numPhotons2): #numphotons2
		
		X,Y,Z = photon_track2[:,i,0].tolist(), photon_track2[:,i,1].tolist(), photon_track2[:,i,2].tolist()
		X.insert(0, point_zero[0])
		Y.insert(0, point_zero[1])
		Z.insert(0, point_zero[2])
		
		
			#every point is a triangle? So the loop measures the number of photons is that array that go from the source triangle to the detector triangles. I have to find the number of photons that go from source triang;e to any triangle on any surface. That surface triangle will be where the photon path's direction is changing if its heading to the detector. If it is not heading to the detector then the
	
		 
		if (X[100] in vertex2[:,0] and Y[100] in vertex2[:,::-1] and Z[100] in vertex2[:,2]): #Y[100] in vertex2[:,1]
			
			if (labelbool2 == False):
			
				ax.plot(X,Y,Z, color='c', label='Detected Photon Path')	
				
				ax.scatter(X,Y,Z, c='y', s=1, label='Detected Photons = ' + str(len(vertex2)))
				labelbool2 = True
				
				
			else:
				ax.plot(X,Y,Z, color='c')
				ax.scatter(X,Y,Z , c='y', s=1)
				
		else:  #This to show the track of undetected photons.
			if (labelbool == False):
				ax.plot(X,Y,Z, color='b', label='Undetected Photon Path')	
				ax.scatter(X,Y,Z , c='r', s=1, label='Last known Position of Photon')
				labelbool = True
				
			else:
				ax.plot(X,Y,Z, color='b')
				ax.scatter(X,Y,Z , c='r', s=1)	
		
	
	

	
	
		

	
	#Aluminum Filler Outline
	theta = np.linspace(-1*np.pi, np.pi, 100)
	Xval = 54*np.cos(theta)+88
	Zval = 50*np.sin(theta)+88
	Yval = 30+8+2.5
	#ax.plot(Xval, Zval, Yval, zdir='y', color='k', label='Aluminum Filler: ' + str(surf.steelSurface.steelAbsorption*100) + '% absorbative')
	#Xval = 50*np.cos(theta)+90
	#Zval = 50*np.sin(theta)+90
	#Yval = 100
	#ax.plot(Xval, Zval, Yval, zdir='y', color='k')
	#ax.plot((55, 55), (30, 100), 140, color='k')
	#ax.plot((55, 55), (30, 100), 40, color='k')
	
	#Fused Silica Window
	Xval = 20*np.cos(theta)+88
	Zval = 20*np.sin(theta)+88
	Yval = 25+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='yellow', label='Fused Silica Window: Refractice Index = ' +str(surf.silicaSurface.silicaEta))
	Xval = 20*np.cos(theta)+88
	Zval = 20*np.sin(theta)+88
	Yval = 29+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='yellow')
	ax.plot((88, 88), (25+8+2.5, 29+8+2.5), 107, color='y')
	ax.plot((88, 88), (25+8+2.5, 29+8+2.5), 69, color='y')
	#Copper plates
	Xval = 30*np.cos(theta)+88
	Zval = 30*np.sin(theta)+88
	Yval = 15+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='g', label='Copper Plate: '+str(surf.CuSurface.cuAbsorption*100)+'% absorb ' + str(surf.CuSurface.cuSpecReflect*100)+'% specular reflect')
	Xval = 30*np.cos(theta)+88
	Zval = 30*np.sin(theta)+88
	Yval = 21+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='g')
	ax.plot((88, 88), (15+8+2.5, 21+8+2.5), 118, color='g')
	ax.plot((88, 88), (15+8+2.5, 21+8+2.5), 58, color='g')
	Xval = 30*np.cos(theta)+88
	Zval = 30*np.sin(theta)+88
	Yval = 37+8+13.9
	ax.plot(Xval, Zval, Yval, zdir='y', color='g')
	Xval = 30*np.cos(theta)+88
	Zval = 30*np.sin(theta)+88
	Yval = 43+8+13.9
	ax.plot(Xval, Zval, Yval, zdir='y', color='g')
	ax.plot((88, 88), (37+8+13.9, 43+8+13.9), 118, color='g')
	ax.plot((88, 88), (37+8+13.9, 43+8+13.9), 58, color='g')
	#Copper rings
	Xval = 19*np.cos(theta)+88
	Zval = 19*np.sin(theta)+88
	Yval = 23+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='purple', label='Fused Silica Holder: '+str(surf.CuSurface.cuAbsorption*100)+'% absorb ' + str(surf.CuSurface.cuSpecReflect*100)+'% specular reflect')
	Xval = 19*np.cos(theta)+88
	Zval = 19*np.sin(theta)+88
	Yval = 25+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='purple')
	ax.plot((88, 88), (23+8+2.5, 25+8+2.5), 107, color='purple')
	ax.plot((88, 88), (23+8+2.5, 25+8+2.5), 69, color='purple')
	Xval = 19*np.cos(theta)+88
	Zval = 19*np.sin(theta)+88
	Yval = 29+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='purple')
	Xval = 19*np.cos(theta)+88
	Zval = 19*np.sin(theta)+88
	Yval = 31+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='purple')
	ax.plot((88, 88), (29+8+2.5,31+8+2.5), 107, color='purple')
	ax.plot((88, 88), (29+8+2.5,31+8+2.5), 69, color='purple')
       
																																																																																																																																																																						
																																																																																												
	#Detector
	ax.plot((85, 91), (65, 65), 91, color='orange')
	ax.plot((85, 85), (65, 65), (85, 91), color='orange')
	ax.plot((91, 91), (65, 65), (85, 91), color='orange')
	
	#teflon reflector 
	Xval = 18*np.cos(theta)+88
	Zval = 18*np.sin(theta)+88
	Yval = 31.5+8+2.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='blue', label='Teflon Reflector: '+str(surf.TefSurface.TefAbsorption*100)+'% absorb ' + str(surf.TefSurface.TefSpecReflect*100)+'% specular reflect')
	Xval = 18*np.cos(theta)+88
	Zval = 18*np.sin(theta)+88
	Yval = 37+8+13.9-0.5
	ax.plot(Xval, Zval, Yval, zdir='y', color='blue')
	ax.plot((88, 88), (31.5+8+2.5,37+8+13.9-0.5), 106, color='blue')
	ax.plot((88, 88), (31.5+8+2.5,37+8+13.9-0.5), 70, color='blue')
	

	ax.set_xlabel('X Label (mm)')
	ax.set_ylabel('Y Label (mm)')
	ax.set_zlabel('Z Label (mm)')
	ax.set_ylim(22,58.9)
	ax.set_xlim(50,130)
	ax.set_zlim(50,130)
	ax.view_init(elev=3., azim=0)
	#plt.savefig('event_display.jpg') 
	plt.title("Photon Track" + '\n' + datetime.date.today().strftime('%B %d, %Y') + '\n' + ' Photons = ' + str(numPhotons2), size=30, y=0.93) #added 11/07/18 #numPhotons 2
	ax.legend(loc='best', fontsize = '14')
	plt.show()
	
	

	
	totAngles = []
	for i in range(len(angles)): #the angles are actually the # of runs lol and the totAngles are the total number of photons detected
		for j in range(len(angles[i])):
			totAngles.append(angles[i][j])
		 	
		
	plot.histogram_2(totAngles,"Incident angles", 1) #change to logscale
	
	#with open("bincount.txt", "wb") as fp:      #saves the list as string format
		#pickle.dump(totAngles, fp)  

'''          
	
	
	with open("bincount.txt", "rb") as fp:       #retrieves the list and converts to int again 
		prev_angle_bins=pickle.load(fp)
	
	it_x=np.arange(0,90)
	y_pos=np.arange(len(it_x))
	#texthere= AnchoredText("placetexthere", loc='bottom')
	plt.hist([prev_angle_bins, totAngles1], y_pos, label=['LXe n=1.69', 'LXe n=1.2'], density=True)
	plt.legend(loc='upper right')
	plt.xlabel('Angles in degrees', fontsize=20)
	plt.ylabel('Counts', fontsize=20)
	plt.title("Difference between Photons hitting the SiPM at different incident angles with LXe n=1.69 vs n=1.2", fontsize=20)
	plt.show()
	
	
	
	countsave1= np.bincount(np.int_(totAngles), weights=None, minlength=90) #outputs a list of the number of counts in each bin, BIN WIDTH MUST BE INTEGER
	#with open("bincount.txt", "wb") as fp:      #saves the list as string format
		#pickle.dump(countsave, fp)            
	with open("bincount.txt", "rb") as fp:       #retrieves the list and converts to int again 
		prev_angle_bins=pickle.load(fp)
	
	#print prev_angle_bins
	
	#print countsave1
	
	neww=countsave1-prev_angle_bins
	#print neww
	it_x=np.arange(0,90)
	#print it_x
	y_pos=np.arange(len(it_x))
	#plt.hist([prev_angle_bins, countsave1], y_pos, label=['w/out tef', 'w/ tef'])
	plt.bar(y_pos,neww, align='center', label='w/ tef')	#Old Version (normalized): plt.bar(y_pos,(neww/total_photons_seen)*100, align='center', label='w/ tef')
	plt.xlabel('Angles in degrees', fontsize=20)
	plt.ylabel('Count Difference %', fontsize=20)
	plt.title("Difference between Photons hitting the SiPM with Fused Silica Refractive Index at 1.59 and 1.61", fontsize=20)
	plt.xticks(y_pos, it_x)
	plt.show()
	


		
	
	

# Making an array for the photons hitting SiPM for all runs to make the different plots below.
vertex = np.array(vertex)
vertexQQ = np.concatenate(vertex)


#bringing back the xyz photons on the SiPM to the center since the SiPM is not at the origin
rishikaiscool =88.1234+0.0294255-0.29127+0.0362488+0.17541  #x axis displacement
rishikaisawesome = 87.98532+0.0156254+0.165738-0.281734+0.17541 #z axis displacement
rishikaisamazing = 42+18.482 #y axis displacement  
x = vertexQQ[:,0]-rishikaiscool     
z = vertexQQ[:,2]-rishikaisawesome
y = vertexQQ[:,1]-rishikaisamazing


plot.histogram_3(z,"Projection",100)

plot.histogram_4(x,"Projection",100)


r = np.sqrt((x)**2 +(z)**2)
plt.scatter(r,totAngles, s = 1, color = 'black')
plt.xlabel('R')
plt.ylabel('Angle')
plt.title('R vs Angle')
plt.show()
	
def step(x):
	return 0.5 * (np.sign(x) + 1)
phi_new = np.arctan((vertexQQ[:,2]-rishikaisawesome)/(vertexQQ[:,0]-rishikaiscool)) * 180 / np.pi + 180*step(-(vertexQQ[:,0]-rishikaiscool))+90
stepAngles = []
banana = []
for i in range(runs):
	banana.append(data.incident_angle(messung_dir[i]))
for i in range(len(banana)):
	for j in range(len(banana[i])):
		stepAngles.append(banana[i][j])




plt.scatter(phi_new,stepAngles, s = 1, color = 'black')
plt.xlabel('Phi')
plt.ylabel('Angle')
plt.title('Phi vs Angle')

plt.show()

plt.scatter(x,z, s = 1, color = 'black')

plt.xlabel('X position (mm)')
plt.ylabel('Z position (mm)')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.gca().set_aspect('equal',adjustable='box')
plt.title('Photon position on SiPM')
plt.show()

#filtering out the high incident angle photons
x_high = []
z_high = []
stepAngle_high = []
for i in range(len(stepAngles)):
	if stepAngles[i] <6 and stepAngles[i] >5 : #>40
		x_high.append(x[i])
		z_high.append(z[i])
		stepAngle_high.append(stepAngles[i])
	#print stepAngle_high[i]
#print len(stepAngles)

plt.scatter(x_high,z_high, s = 1, color = 'black')
plt.xlabel('X position (mm)')
plt.ylabel('Z position (mm)')
plt.title('Photon Position on SiPM between Incident Angles between 6 and 7 degrees')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()

xx = np.array(x_high)
zz = np.array(z_high)
r_high = np.sqrt((xx)**2 +(zz)**2)
plt.scatter(r_high,stepAngle_high, s = 1, color = 'black' )
plt.xlabel('R High')
plt.ylabel('High Angles')
plt.title('R position for High incident Angles')

plt.show()



#print r_high
#print stepAngle_high

plt.hist2d(x ,z, bins =200, cmap='hot_r')

plt.title('Photon Position on SiPM')
plt.xlabel('X Position (mm)')
plt.ylabel('Z Position (mm)')
plt.colorbar()
plt.xlim(-3,3)
plt.ylim(-3,3)

plt.show()
plt.hist2d(x_high ,z_high, bins =200, cmap='hot_r')

plt.xlabel('X_pos')
plt.ylabel('Z_pos')
plt.colorbar()
plt.xlim(-3,3)
plt.ylim(-3,3)

plt.show()




# Making the plot of the last known position of each photons in the setup
endPosRotated0 = photons3.pos[detected3]
endPosRotatedR = photons3.pos[RayleighScattering3]    #added 18/07/18
endPosRotated = photons3.pos[absorbB3]
endPosRotated2 = photons3.pos[absorbS3]     
endPosRotated3 = photons3.pos[ReflectDiffusion3]     #added 18/07/18
endPosRotated4 = photons3.pos[SpecularReflection3]


fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(endPosRotatedR[:,0], endPosRotatedR[:,1], endPosRotatedR[:,2], c='k', label='Rayleigh Scattering')  # Rayleigh scattering
ax.scatter(endPosRotated[:,0], endPosRotated[:,1], endPosRotated[:,2], c='r', label='Bulk Absorption')     #bulk absorption
ax.scatter(endPosRotated2[:,0], endPosRotated2[:,1], endPosRotated2[:,2], c='green', label='Surface Absorption')  #surface absorption
ax.scatter(endPosRotated3[:,0], endPosRotated3[:,1], endPosRotated3[:,2], c='b', label='Diffuse Reflection')  #diffuse
ax.scatter(endPosRotated4[:,0], endPosRotated4[:,1], endPosRotated4[:,2], c='orange', label='Specular Reflection') #Specular Reflected commented as all specularly reflected photons are absorbed in a different way as well
ax.scatter(endPosRotated0[:,0], endPosRotated0[:,1], endPosRotated0[:,2], c='y', label='Photons Detected')  #photons detected

ax.set_xlabel('X Label (mm)')
ax.set_ylabel('Y Label (mm)')
ax.set_zlabel('Z Label (mm)')
#ax.set_ylim(0,45)
#ax.set_xlim(35,45)
plt.title(ax.title, y=1)
ax.set_title('Photon Distribution in Cell' + '\n' + datetime.date.today().strftime('%B %d, %Y') + '\n' + ' Photons = ' + str(numPhotons3))
ax.title.set_fontsize(30)
#ax.set_ylim(34,67)
ax.legend(loc='best',fontsize = '14')

plt.show()
'''		


################# END ##################################




print ("=====================================================================")
print ("  Finish Simulation				Done") 
print ("  Time elapsed					", time.time()-start_begin, "sec" )
print ("=====================================================================")



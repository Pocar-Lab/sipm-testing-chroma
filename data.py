#!/usr/bin/env python
from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def incident_angle(last_pos):
	angles = np.arccos(np.fabs(last_pos[:,1])/np.sqrt((last_pos[:,0]**2 + last_pos[:,1]**2 + last_pos[:,2]**2)))*(180/np.pi)
	return angles

def inner_radius(mesh, arg1, arg2):
	meshT = mesh.get_triangle_centers()
	r_min = min(np.sqrt(pow(meshT[:,0],2) + pow(meshT[:,2],2)))
	new = np.where(np.sqrt(pow(meshT[:,0],2) + pow(meshT[:,2],2)) < (r_min+.2), arg1, arg2)
	return new
	
def radius_bottom(mesh,arg1, arg2):
	meshT = mesh.get_triangle_centers()
	r_max = max(np.sqrt(pow(meshT[:,0],2) + pow(meshT[:,2],2)))
	new = np.where((np.sqrt(pow(meshT[:,0],2) + pow(meshT[:,2],2)) < (r_max-0.03)) & (meshT[:,1] >.35), arg1, arg2)
	return new
	
def bottom(mesh, arg1, arg2):
	meshT = mesh.get_triangle_centers()
	bot = min(meshT[:,1])
	new = np.where(meshT[:,1]<(bot+.3), arg1, arg2)
	return new
	
def top(mesh, arg1, arg2):
	meshT = mesh.get_triangle_centers()
	bot = max(meshT[:,1])
	new = np.where(meshT[:,1]>(bot-.01), arg1, arg2)
	return new

def get_center(mesh):
	meshT = mesh.get_triangle_centers()
	pos = [np.mean(meshT[:,0]), np.mean(meshT[:,1]), np.mean(meshT[:,2])]
	return pos 

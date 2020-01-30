#!/usr/bin/env python

from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import seaborn as sns
from scipy.stats import *
#from ROOT import gROOT, TCanvas, TF1, TH1F, TFile, TTree, TH2F, gStyle
import umass 

from matplotlib.offsetbox import AnchoredText

'''
def scatter_hist(x,y):
	fig = plt.figure(figsize=(10, 10))
	plt.clf()
	nullfmt = NullFormatter()
	left, width = 0.1, 0.65				
	bottom, height = 0.1, 0.65
	bottom_h = left_h = left+width+0.02
	rect_scatter = [left, bottom, width, height]
	rect_histx = [left, bottom_h, width, 0.2]
	rect_histy = [left_h, bottom, 0.2, height]
	plt.figure(1, figsize=(10,10))			
	axScatter = plt.axes(rect_scatter)
	axHistx = plt.axes(rect_histx)
	axHisty = plt.axes(rect_histy)
	axHistx.xaxis.set_major_formatter(nullfmt)	
	axHisty.yaxis.set_major_formatter(nullfmt)
	axScatter.scatter(x, y)						
	binwidth = 1						
	xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
	lim = (int(xymax/binwidth)+1) * binwidth
	axScatter.set_xlim(0, max(x)+2)
	axScatter.set_ylim(0, max(y)+2)
	bins = np.arange(0, lim + binwidth, binwidth)
	axHistx.hist(x, bins=bins)
	axHisty.hist(y, bins=bins, orientation='horizontal')
	axHistx.set_xlim(axScatter.get_xlim())
	axHisty.set_ylim(axScatter.get_ylim())
	plt.title("Scatter_hist") #added 11/07/18
	plt.show()
	
def histogram(data, xlabel, bin_nr):
	fig = plt.figure(figsize=(10,8))
#	sns.axlabel(xlabel, "counts [#]")
#	g = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	g.set_xlabel('Number of Photons',size=30)
	g.set_ylabel("Number of Occurrences",size=30)
	plt.title("Detected Photons",size=30) #added 11/07/18
	plt.show()	

def histogram(data,xlabel,bin_nr):
	axs.hist(data, bins=bin_nr)


#added 26/7/18
def histogram_2(data, xlabel, bin_nr):
	fig = plt.figure(figsize=(20,18))
#	sns.axlabel(xlabel, "counts [#]")
	#r = sns.distplot(data, bins=bin_nr, kde=False, rug=False, color='b', norm_hist=False)
	data, bin_nr, xlabel = plt.hist(data, 
	r.set_xlabel('angles in Degrees',size=30)
	r.set_ylabel("Number of Occurrences",size=30)
	r.tick_params(axis = "x" , which = "major" , labelsize = 10)
	r.tick_params(axis = "y" , which = "major" , labelsize = 10)
	r.set_xticks(np.arange(0,90, 1))
	#r.set_yscale('log')
	plt.title("Incident angles of Photons Detected",size=30) #added 11/07/18
	plt.show()
'''
def histogram_2(data, xlabel, bw):
	fig = plt.figure(figsize=(20,18))
	ax = fig.add_subplot(111)
	#(histdat, xentr,patches) = plt.hist(data,bins , range=(0,90))
	#normdata = [x / bw for x in histdat]
	#normdata = normdata.append(0)
	#print bins, len(xentr), len(normdata)
	#x = range(22)
	#plt.plot(x,normdata)
	plt.hist(data,bins = 90/bw , range=(0,90)) #normalization: density=True
	ax.set_xlabel('angles in Degrees',size=30)
	ax.set_ylabel('Number of Occurrences',size=30)
	ax.tick_params(axis = "x" , which = "major" , labelsize = 10)
	ax.tick_params(axis = "y" , which = "major" , labelsize = 10)
	ax.set_xticks(np.arange(0,90, 1))
	#plt.yscale('log')
	plt.title("Incident angles of Photons Detected",size=30)
	plt.show()

'''
def histogram_3(data, xlabel, bin_nr):
	fig = plt.figure(figsize=(18,13))
#	sns.axlabel(xlabel, "counts [#]")
	#i = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	i.set_xlabel('Z-axis Projection (mm)',size=30)
	i.set_ylabel("Number of Occurrences",size=30)
	i.tick_params(axis = "x" , which = "major" , labelsize = 25)
	i.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("Z-axis Projection",size=30) #added 11/07/18
	#i.set_xlim(85,92)
	plt.show()
'''

def histogram_3(data, xlabel, bins):
	fig = plt.figure(figsize=(18,13))
	ax = fig.add_subplot(111)
	plt.hist(data, bins=bins)
	ax.set_xlabel('Z-axis Projection (mm)',size=30)
	ax.set_ylabel("Number of Occurrences",size=30)
	ax.tick_params(axis = "x" , which = "major" , labelsize = 25)
	ax.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("Z-axis Projection",size=30) 
	plt.show()
'''
def histogram_4(data, xlabel, bin_nr):
	fig = plt.figure(figsize=(18,13))
#	sns.axlabel(xlabel, "counts [#]")
	#q = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	q.set_xlabel('X-axis Projection (mm)',size=30)
	q.set_ylabel("Number of Occurrences",size=30)
	q.tick_params(axis = "x" , which = "major" , labelsize = 25)
	q.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("x-axis Projection",size=30) #added 11/07/18
	#i.set_xlim(85,92)
	plt.show()
'''
def histogram_4(data, xlabel, bins):
	fig = plt.figure(figsize=(18,13))
	ax = fig.add_subplot(111)
	plt.hist(data, bins=bins)
	ax.set_xlabel('X-axis Projection (mm)',size=30)
	ax.set_ylabel("Number of Occurrences",size=30)
	ax.tick_params(axis = "x" , which = "major" , labelsize = 25)
	ax.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("X-axis Projection",size=30) 
	plt.show()

'''
def histogram_5(data, ylabel, bin_nr):
	fig = plt.figure(figsize=(18,13))
#	sns.axlabel(xlabel, "counts [#]")
	m = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	m.set_xlabel('Y-axis Projection (mm)',size=30)
	m.set_ylabel("Number of Occurrences",size=30)
	m.tick_params(axis = "x" , which = "major" , labelsize = 25)
	m.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("Y-axis Projection",size=30) #added 11/07/18
	#i.set_xlim(85,92)
	plt.show()
def event_display(numPhotons, photon_track, vertex, o_center, v_center, BIloc):
	fig = plt.figure(figsize=(18,13))
	ax = fig.add_subplot(111, projection='3d')
	for i in range(numPhotons):
		
		X,Y,Z = photon_track[:,i,0].tolist(), photon_track[:,i,1].tolist(), photon_track[:,i,2].tolist()
		X.insert(0, BIloc[0])
		Y.insert(0, BIloc[1])
		Z.insert(0, BIloc[2])
		ax.plot(X,Y,Z, color='b')	
		ax.scatter(X,Y,Z , c='r', s=.5)		
		

	#ax.plot_wireframe(o_center[::20,0], o_center[::20,1], o_center[::20,2])
	#ax.plot_wireframe(v_center[::20,0], v_center[::20,1], v_center[::20,2]) #o_centre is the centre of the source and v_centre is the centre of the detector #added 11/07/18
	ax.scatter(vertex[:,0], vertex[:,1], vertex[:,2], c='y', s=5)	
	#plt.ylim(30,60)
	#plt.xlim(30,90)
	#ax.set_zlim(0,200)
	ax.set_xlabel('X Label (mm)')
	ax.set_ylabel('Y Label (mm)')
	ax.set_zlabel('Z Label (mm)')
	ax.view_init(elev=3., azim=0)
	plt.savefig('event_display.jpg') 
	plt.title("Photon Track", size=30) #added 11/07/18
	plt.show()	
	
def color_map(hist):
	c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )	
	gStyle.SetPalette(1)
	gStyle.SetOptStat(0)
	gStyle.SetNumberContours(64)
	hist.Draw("colz")
	hist.GetXaxis().SetTitle("radius [mm]")
	hist.GetYaxis().SetTitle("distance from center [mm]")
	c1.SaveAs("light_collection_map.jpg")	



	i.tick_params(axis = "x" , which = "major" , labelsize = 25)
	i.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("Z-axis Projection",size=30) #added 11/07/18
	#i.set_xlim(85,92)
	
	plt.show()
def histogram_4(data, xlabel, bin_nr):
	fig = plt.figure(figsize=(18,13))
#	sns.axlabel(xlabel, "counts [#]")
	q = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	q.set_xlabel('X-axis Projection (mm)',size=30)
	q.set_ylabel("Number of Occurrences",size=30)
	q.tick_params(axis = "x" , which = "major" , labelsize = 25)
	q.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("x-axis Projection",size=30) #added 11/07/18

	#i.set_xlim(85,92)
	plt.show()
def histogram_5(data, ylabel, bin_nr):
	fig = plt.figure(figsize=(18,13))
#	sns.axlabel(xlabel, "counts [#]")
	m = sns.distplot(data, bins=bin_nr, kde=False, rug=False, norm_hist=False)
	m.set_xlabel('Y-axis Projection (mm)',size=30)
	m.set_ylabel("Number of Occurrences",size=30)
	m.tick_params(axis = "x" , which = "major" , labelsize = 25)
	m.tick_params(axis = "y" , which = "major" , labelsize = 25)
	plt.title("Y-axis Projection",size=30) #added 11/07/18
	#i.set_xlim(85,92)
	plt.show()
def event_display(numPhotons, photon_track, vertex, o_center, v_center, BIloc):
	fig = plt.figure(figsize=(18,13))
	ax = fig.add_subplot(111, projection='3d')
	for i in range(numPhotons):
		
		X,Y,Z = photon_track[:,i,0].tolist(), photon_track[:,i,1].tolist(), photon_track[:,i,2].tolist()
		X.insert(0, BIloc[0])
		Y.insert(0, BIloc[1])
		Z.insert(0, BIloc[2])
		ax.plot(X,Y,Z, color='b')	
		ax.scatter(X,Y,Z , c='r', s=.5)		
		

	#ax.plot_wireframe(o_center[::20,0], o_center[::20,1], o_center[::20,2])
	#ax.plot_wireframe(v_center[::20,0], v_center[::20,1], v_center[::20,2]) #o_centre is the centre of the source and v_centre is the centre of the detector #added 11/07/18
	ax.scatter(vertex[:,0], vertex[:,1], vertex[:,2], c='y', s=5)	
	#plt.ylim(30,60)
	#plt.xlim(30,90)
	#ax.set_zlim(0,200)
	ax.set_xlabel('X Label (mm)')
	ax.set_ylabel('Y Label (mm)')
	ax.set_zlabel('Z Label (mm)')
	ax.view_init(elev=3., azim=0)
	plt.savefig('event_display.jpg') 
	plt.title("Photon Track", size=30) #added 11/07/18
	plt.show()	
	
def color_map(hist):
	c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )	
	gStyle.SetPalette(1)
	gStyle.SetOptStat(0)
	gStyle.SetNumberContours(64)
	hist.Draw("colz")
	hist.GetXaxis().SetTitle("radius [mm]")
	hist.GetYaxis().SetTitle("distance from center [mm]")
	c1.SaveAs("light_collection_map.jpg")	

'''


#!/usr/bin/env python
#***************************************************************************
import sys, getopt, time
import arguments as arg
from chroma import make, view, optics, sample, gpu
from chroma.camera import Camera, EventViewer
from chroma.demo.optics import glass, water, vacuum, black_surface, r7081hqe_photocathode
from chroma.detector import Detector
from chroma.event import Photons
from chroma.generator import vertex
from chroma.geometry import Geometry, Material, Solid, Surface, Mesh
#from chroma.io.root import RootWriter
from chroma.pmt import build_pmt
from chroma.sample import uniform_sphere
from chroma.sim import Simulation
from chroma.stl import mesh_from_stl
from chroma.transform import make_rotation_matrix, make_rotation_matrix, get_perp, rotate, rotate_matrix, normalize
from chroma.loader import create_geometry_from_obj, load_bvh
#from ROOT import gROOT, TCanvas, TF1, TH1F, TFile, TTree, TH2F, gStyle
#***************************************************************************
from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D
#***************************************************************************
import Materials as mat
import Surfaces as surf
import numpy as np
#import setupMaterials as sm
import chroma.event as chromaev
import matplotlib
import matplotlib.pyplot as plt
#import pandas as pd
from scipy import stats, integrate
#import seaborn as sns
#from mpl_toolkits.mplot3d import Axes3Df
import data as data
#***************************************************************************

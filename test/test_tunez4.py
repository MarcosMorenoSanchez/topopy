# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:36:31 2018

@author: Usuario
"""

from topopy import DEM, Network, BNetwork, Grid, TProfile, canal_2_profile
import ogr
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Number of basins
nbasins = 33

# Get network and basins
basedir = "C:/Users/Usuario/Desktop/tunez/gisdata/chi_analysis"
bnet = BNetwork(basedir + "/bnet_04.net")
perfiles = []

for n in range(1, 34):
    bnet = BNetwork(basedir + "/bnet_{:02}.net".format(n))
    bnet.calculate_chi(0.3)
    canal = bnet.get_main_channel()
    perfil = canal_2_profile(canal, bnet, n)
    perfiles.append(perfil)
    
np.save(basedir + "/perfiles_tunez.npy", np.array(perfiles))
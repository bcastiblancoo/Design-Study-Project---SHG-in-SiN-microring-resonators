# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 11:43:32 2025

@author: PC
"""

import emodeconnection as emc
import numpy as np

EMODE_CMD = r"C:\Program Files\EModePhotonix\EMode\EMode.exe"

## Set simulation parameters
dx, dy = 10, 10 # [nm] resolution
h_core = 500 # [nm] waveguide core height
h_clad = 1000 # [nm] waveguide top and bottom clad
w_core = 1000 # [nm] waveguide core width
w_trench = 1000 # [nm] waveguide side trench width
window_width = w_core + w_trench*2 # [nm]
window_height = h_core + h_clad*2 # [nm]
num_modes = 1 # [-] number of modes
boundary = 'TE'

# FH Generation:
#wav_nm_ = np.arange(1520, 1600, 5) # [nm]    

# SH Generation:
wav_nm_ = np.arange(760, 800, 2.5) # [nm]

## Connect and initialize EMode
em = emc.EMode(emode_cmd=[EMODE_CMD], simulation_name ='dispersionSiN_SH')

## Settings
em.settings(
    x_resolution = dx, y_resolution = dy,
    window_width =window_width,
    window_height = window_height,
    num_modes = num_modes, boundary_condition = boundary,
    background_material = 'SiO2',
    expansion_resolution = 20, expansion_size = 1500)

## Draw shapes
em.shape(name = 'BOX', material = 'SiO2', height = h_clad)
em.shape(name = 'core', material = 'SiN', height = h_core,
    etch_depth = h_core*3/4, mask = w_core, sidewall_angle = 15)

## Run wavelength sweep
data = em.sweep(key = 'wavelength', values = wav_nm_,
    result = ['effective_index'])

em.report()

em.plot()

## Close EMode
em.close()

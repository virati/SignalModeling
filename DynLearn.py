#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:36:13 2017

@author: virati
Trying to reconstruct a dynamical system from a time series
Synthetic attempt, but should be translatable to empirical time series
"""

import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

def rk4(odes, state, parameters, dt=0.01):
    k1 = dt * odes(state, parameters)
    k2 = dt * odes(state + 0.5 * k1, parameters)
    k3 = dt * odes(state + 0.5 * k2, parameters)
    k4 = dt * odes(state + k3, parameters)
    
    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def generate(nlength,odes,state,parameters):
    data = np.zeros([state.shape[0], nlength])
    
    for i in range(5000):
        state = rk4(odes,state,parameters)
        
    for i in range(nlength):
        state = rk4(odes,state,parameters)
        data[:,i] = state
    
    return data

def lorenz_odes(state,params):
    x = state[0]
    y = state[1]
    z = state[2]
    
    sigma = params[0]
    rho = params[1]
    beta = params[2]
    
    return np.array([sigma*(y-x),x*(rho-z)-y,x*y - beta * z])

def lorenz_generate(nlength):
    return generate(nlength,lorenz_odes, np.array([-8.0,8.0,27.0]),np.array([10.0,8/3.0,28.0]))

data = lorenz_generate(2**13)
plt.plot(data[0,:])
plt.show()

from mpl_toolkits.mplot3d.axes3d import Axes3D
#%%

plt.figure()
ax = plt.axes(projection='3d')
ax.plot(data[0,:],data[1,:],data[2,:])

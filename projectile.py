# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 15:47:51 2016

Creates an animation of projectile motion without friction

@author: Eliezer
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

g = 9.8                                                        #acceleration due to gravity

v = 10.0                                                       #initial velocity (m/s)
theta = 65.0                                                   #initial angle of launch in degrees
theta = theta * np.pi / 180.0

line, = ax.plot([],c='k')   # plots line trailing the projectile
point, = ax.plot([],c='k',marker='o') # plots the projectile

def init():
    line.set_data([],[])
    point.set_data([],[])
    return line, point,
    
def animate(i):
    t = np.arange(0, i, 0.01)
    xi = v * np.cos(theta) * (t/100.0)
    yi = v * np.sin(theta) * (t/100.0) - (0.5) * g * (t/ 100.0)**2
    point.set_data(xi[-1],yi[-1])
    line.set_data(xi,yi)
    return line, point,

tmax = 2*v/g * 100.0
plt.axis([0.0, 11.0, 0.0, 5.0])
#ax.set_autoscale_on(False)
xlim = ax.get_xlim()


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=False,
                              interval=20, frames = int(tmax))
plt.show()
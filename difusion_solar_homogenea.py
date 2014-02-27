# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>


import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import math
n = int(sys.argv[1])
r0 = 100.0
pasos = np.zeros(n)
for i in range(n):
    k = 0
    x = random.uniform(-r0,r0)
    y = random.uniform(-r0,r0)
    z = random.uniform(-r0,r0)
    r = math.sqrt(x**2+y**2+z**2)
    while(r < r0):
        theta = np.random.uniform(0,1)*2*math.pi
        phi = np.random.uniform(0,1)*math.pi - math.pi/2
        x = x + math.cos(phi)*math.cos(theta)
        y = y + math.cos(phi)*math.sin(theta)
        z = z + math.sin(phi)
        r = math.sqrt(x**2 + y**2 + z**2)
        k = k + 1
    pasos[i] = k

plt.hist(pasos, 20, (0,max(pasos)))
plt.savefig("histo_difusion_solar_homogenea_"+str(n)+".pdf")

    


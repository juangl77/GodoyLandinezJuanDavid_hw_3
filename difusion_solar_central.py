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
    r = 0.0
    x = 0.0
    y = 0.0
    z = 0.0
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
plt.savefig("histo_difusion_solar_central_"+str(n)+".pdf")

    


# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>
import sys
import numpy as np
import matplotlib.pyplot as plt
minx = -2.0
maxx = 2.0
miny = -2.0
maxy = 2.0
M = np.zeros((1024,1024), dtype = np.uint8)
for i in range(M.shape[1]):
    for j in range(M.shape[0]):
        x1 = (i*((maxx-minx)/float(M.shape[1]))) + minx
        y1 = (j*((maxy-miny)/float(M.shape[0]))) + miny
        x = 0.0
        y = 0.0
        n = int(sys.argv[1])
        k = 0.0
        while(k < n and x**2 + y**2 < 4):
            temp = x**2 - y**2 + x1
            y = y1 + 2*x*y
            x = temp
            k = k +1
        M[j][i] = k

plt.imshow(M, extent = (minx, maxx, miny, maxy))
plt.savefig("mandelbrot_"+str(n)+".pdf")
# <codecell>


# <codecell>



# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import math
import sys
import numpy as np
import matplotlib.pyplot as plt

n = int(sys.argv[1])
ang = np.random.rand(n)*2*math.pi
x = np.cumsum(np.cos(ang))
y = np.cumsum(np.sin(ang))
d = np.sqrt(x**2+y**2)
plt.plot(np.log(range(0,n)),np.log(d))
plt.savefig("Browniano_2D_"+str(n)+".pdf")

# <codecell>


# <codecell>



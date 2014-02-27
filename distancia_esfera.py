# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy as np
import math
import sys

lat1 = float(sys.argv[1])
lon1 = float(sys.argv[2])
lat2 = float(sys.argv[3])
lon2 = float(sys.argv[4])

theta = (lat1-lat2)*math.pi/180.0
phi = (lon1-lon2)*math.pi/180
r = 6371

d = r*math.acos(1 - (math.sin(theta)**2 + math.sin(phi)**2)/2)
print d


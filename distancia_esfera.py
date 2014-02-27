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

theta1 = math.pi/2 - lat1*math.pi/180.0
theta2 = math.pi/2 - lat2*math.pi/180.0
phi = (lon1-lon2)*math.pi/180.0
r = 6378.137
alpha = math.acos(math.cos(theta1)*math.cos(theta2)+math.sin(theta1)*math.sin(theta2)*math.cos(phi))
x = alpha*r
print x


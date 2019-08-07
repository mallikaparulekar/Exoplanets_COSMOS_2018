# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import numpy as np

total = 0
inRange = 0
num = []
radius = []
rocky = 0

with open(r"C:\Users\Rupsa\Desktop\COSMOS\Project\Data\planetRadius.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if row[1] != "":
            num.append(float(row[0]))
            radius.append(float(row[1]))
for i in range(len(radius)):
    radius[i] = radius[i]/0.08921


plt.hist(radius, np.arange(0,8,0.1))
plt.xlabel("Planet Radius (Earth Radii)")
plt.ylabel("Frequency")

for r in radius:
    if r<3.9:
        rocky+=1
print(str(rocky/len(radius)))

'''
total = len(num)
for r in radius:
    if r <= earth:
        inRange+=1
print(str(inRange/total))

loc_rowid	pl_radj	pl_radjerr1	pl_radjerr2	pl_radjlim
'''
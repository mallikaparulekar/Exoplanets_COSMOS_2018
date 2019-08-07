# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import numpy as np

total = 0
starAge = []
nums = []
starMetal = []
starMass = []

with open(r"C:\Users\Rupsa\Desktop\COSMOS\Project\Data\starCharacteristics.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if row[3] != "" and row [4] != "" and row [6] != "":
            nums.append(float(row[0]))
            starMass.append(float(row[3]))
            starMetal.append(float(row[4]))
            starAge.append(float(row[6]))

plt.hist(starAge, np.arange(0,14,0.2))
plt.show()

plt.hist(starMetal, np.arange(-0.8, 0.6, 0.05))
plt.show()

plt.hist(starMass, np.arange(0, 4, 0.1))
plt.xlabel("Star Mass (Solar Mass)")
plt.ylabel("Frequency")
plt.show()

hStarAge = []
hNums = []
hStarMetal = []
hStarMass = []

with open(r"C:\Users\Rupsa\Desktop\COSMOS\Project\Data\17PlanetStars.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        hNums.append(float(row[2]))
        if row[3] != "":
            hStarMass.append(float(row[3]))
        if row[4] != "":
            hStarMetal.append(float(row[4]))
        if row[6] != "":
            hStarAge.append(float(row[6]))

plt.hist(hStarAge)
plt.show()

plt.hist(hStarMetal)
plt.show()

plt.hist(hStarMass)
plt.xlabel("Star Mass (Solar Mass)")
plt.ylabel("Frequency")
plt.show()

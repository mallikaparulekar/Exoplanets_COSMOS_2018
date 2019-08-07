# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

num = []
temps = []
lumLogs = []
ranges = []
lums = []
distances = []
normalized = []
habitable = 0
planetRadius = []
habitNums = []

def innerBound(temp,lum):
    return (0.72-(0.000027619*(temp-5700))-(0.0000000038095*((temp-5700)**2)))*(math.sqrt(lum))
def outerBound(temp,lum):
    return (1.77-(0.00013786*(temp-5700))-(0.0000000014286*((temp-5700))**2))*(math.sqrt(lum))

with open(r"C:\Users\Rupsa\Desktop\COSMOS\Project\Data\habitZone.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if row[1] != "":
            if row[2] != "":
                if row[3] != "":
                    if row[5]!= "":
                        num.append(float(row[0]))
                        temps.append(float(row[2]))
                        lumLogs.append(float(row[3]))
                        distances.append(float(row[1]))
                        planetRadius.append(float(row[5]))
for i in range(len(lumLogs)):
    lums.append(10**lumLogs[i])
for j in range(len(lums)):
    ranges.append([innerBound(temps[j],lums[j]), outerBound(temps[j],lums[j])])

for i in range(len(planetRadius)):
    planetRadius[i] = planetRadius[i]/0.08921

for n in range(len(distances)):
    normalized.append((distances[n]-ranges[n][0])/(ranges[n][1]-ranges[n][0]))

for x in range(len(num)):
    if normalized[x] >= 0 and normalized[x] <= 1:
        if planetRadius[x] < 1.7:
            habitNums.append(num[x])

print(habitNums)
print(str(len(habitNums)/(len(num))))
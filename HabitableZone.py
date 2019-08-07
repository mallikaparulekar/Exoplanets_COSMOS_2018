# -*- coding: utf-8 -*-
import math
import csv
import matplotlib.pyplot as plt

num = []
temps = []
lumLogs = []
ranges = []
lums = []
distances = []
normalized = []
habitable = 0
planetRadius = []

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



plt.scatter(normalized, planetRadius)
plt.xlabel("Normalized Distance from Star")
plt.ylabel("Planet Radius (Earth Radii)")
plt.plot(((1-innerBound(5777,1))/(outerBound(5777,1)-innerBound(5777,1))), 1, 'ro')
#plt.annotate("Earth", xy=(((1-innerBound(5777,1))/(outerBound(5777,1)-innerBound(5777,1))), 1), xytext=(0.25,0.6), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.plot(((1.524-innerBound(5777,1))/(outerBound(5777,1)-innerBound(5777,1))), 0.531, 'ro')
#plt.annotate("Mars", xy=(((1.524-innerBound(5777,1))/(outerBound(5777,1)-innerBound(5777,1))), 0.531), xytext=(0.7,0.2), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.xlim(-1,2)
plt.ylim(0,5)
plt.savefig(r"C:\Users\Rupsa\Desktop\COSMOS\Project\Graphs\HSvsRadius.png")
'''

for k in range(len(distances)):
    if distances[k] >= ranges[k][0] and distances[k] <= ranges[k][1]:
        habitable += 1

plt.figure()
plt.hist(distances, np.arange(1,150))
plt.figure()
plt.scatter(distances, starSize)
plt.xlim([0,10])

print(habitable/len(num))
'''

        
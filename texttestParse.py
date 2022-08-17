import matplotlib.pyplot as plt
import numpy as np
import sys

testresultsFile = str(sys.argv[1])
imageFileName = str(sys.argv[2])

file = open(testresultsFile)
data = file.readlines()
xRaw = np.array(data[0].split(",")[::-1])
yRaw = np.array(data[1].split(",")[::-1])



xFixed= []
for val in xRaw:
    if val != '':
        xFixed.append(float(val)) 

xFixed = xFixed[::-1]



yFixed= []
for val in yRaw:
    if val != '':
        yFixed.append(float(val)) 
   
yFixed = yFixed[::-1]

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


default_x_ticks = range(len(xFixed)) 
plt.plot(xFixed, yFixed)
plt.savefig(imageFileName, bbox_inches='tight')


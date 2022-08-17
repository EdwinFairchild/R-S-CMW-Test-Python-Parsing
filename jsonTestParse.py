import json  
from matplotlib import pyplot as plt
import numpy as np
import sys
# Opening JSON file
testresultsFile = str(sys.argv[1])
imageFileName = str(sys.argv[2])


f = open(testresultsFile)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
xRaw = data['SubElements'][8]['TestCases'][0]['Elements'][1]['Measured'][0]['Values'][0]['Value']
xRaw = xRaw.split(',')

xFixed= []
for val in xRaw:
    if val != '':
        xFixed.append(float(val)) 

xFixed = xFixed[::-1]

yRaw = data['SubElements'][8]['TestCases'][0]['Elements'][1]['Measured'][0]['Values'][1]['Value']
yRaw = yRaw.split(',')

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


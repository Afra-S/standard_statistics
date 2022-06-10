import numpy as np
import sys
import subprocess
import math

from scipy.stats import circmean
from scipy.stats import circstd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.plotly as py
from matplotlib import cm


logang1=False
logdata1=input("MD data or experimental data? [MD/exp] ")
name1=input("Enter name file data ")

if(logdata1.lower()=='md'):
    tet=input("Are you considering angular averages or angles time series?[Y/N] ")
    if(tet.lower()=='y'):
        logang1=True

file1=open(name1,'r')
h=3510000
data1=np.zeros((h))
ki=-1
for line in file1:
    ki=ki+1
    #print(line)
    data1[ki]=float(line)

xdata= data1[0:ki+1]

if(logang1==True):
    ave=circmean(xdata*math.pi/180.0,low=-math.pi,high=math.pi)*180/math.pi
    sigma=circstd(xdata*math.pi/180.0,low=-math.pi,high=math.pi)*180/math.pi
else:
    ave=np.mean(xdata)
    sigma=np.std(xdata)

print('Average value: ',ave)
print('Sigma: ',sigma)

let=input("Are you considering time series?[Y/N] ")

if(let.lower()=='y'):
    if(logang1==True):
        num_bins=720
    else:
        num_bins= 20 #int(1+3.322*math.log10(ki*1.0+1)) #Modify if needed

    #generate bins boundaries and heights
    bin_height,bin_boundary = np.histogram(xdata,bins=num_bins)
    #define width of each column
    width = bin_boundary[1]-bin_boundary[0]
    #standardize each column by dividing with the maximum height
    bin_height = bin_height/(ki+1)
    #plot
    plt.bar(bin_boundary[:-1],bin_height,width = width)
    #n, bins, patches = plt.hist(xdata, num_bins,normed=1, facecolor='blue',alpha=0.5)
    #plt.plot(bins, y, 'r--')
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()

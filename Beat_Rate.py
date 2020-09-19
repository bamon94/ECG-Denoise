# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:44:02 2020

@author: bhara
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

ecg = scipy.io.loadmat('givenECG3.mat')['givenECG3'].squeeze()
fs = 360
ts = np.arange(0,3600*1/fs,1/fs)
plt.figure()
plt.plot(ts,ecg)
plt.xlabel('time')
plt.ylabel('amplitude')
index = np.argwhere(ecg>1100).squeeze()
rIndexList = []
subListIndices = np.argwhere(np.diff(index)>1).squeeze()
prevI = 0

subLists = np.split(index,subListIndices+1)

for l in subLists:
    maxValue = 0 
    for j in l:
        if ecg[j] > maxValue:
            maxValue = ecg[j]
            maxIndex = j
    rIndexList.append(j)
rIndexArray = np.array(rIndexList)
beatRate = 1/fs* np.diff(rIndexArray)
time = 0
timeList = []
for t in beatRate:
    time = time + t
    timeList.append(time)
    
plt.figure()
plt.plot(timeList,beatRate)
plt.xlabel('time')
plt.ylabel('BeatRate')
plt.show()
mean = np.mean(beatRate)
sd = np.std(beatRate)


        



        
        
            
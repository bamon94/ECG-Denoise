# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:41:04 2020

@author: bhara
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

ecg = scipy.io.loadmat('inputECG.mat')['inputECG'].squeeze()
fs = 360
N = ecg.shape[0]
ts = np.arange(0,N*1/fs,1/fs)
#contFreq = np.arange(0,(N-1)*fs/N,fs/N)

n = 200
noise = np.random.randn(n,N)
noisySignals = ecg + noise
prdList = []

for i in range(n):
    reconstructedSignal = (1/(i+1)) * np.sum(noisySignals[0:(i+1),:],0)
    ms = (1/N)*np.sum(ecg**2)
    msd = (1/N)*np.sum((reconstructedSignal - ecg)** 2)
    prd = ((msd/ms)**0.5)*100
    prdList.append(prd)
   
prdArray = np.array(prdList)
plt.figure();
plt.xlabel('Iteration number')
plt.ylabel('Root Mean Sqared Error')
plt.plot(np.arange(1,n+1,1),prdArray)
    


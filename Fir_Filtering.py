# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:45:24 2020

@author: bhara
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def firFilter(window,N,ecg,ts,fs,ecgNoisy):
    numTaps = 501
    #h1 = signal.firwin(numTaps, cutoff = 1, window = window,pass_zero=False,fs = fs)
    #h2 = signal.firwin(numTaps, cutoff = [49,51], window = window,pass_zero=True,fs = fs)
    h1 = signal.firwin(numTaps, cutoff =[0.9,1.1], window = window,pass_zero=True,fs = fs)
    #h2 = signal.firwin(numTaps, cutoff = [49,51], window = window,pass_zero=True,fs = fs)
    h2 = signal.firwin(numTaps, cutoff = [49,51], window = window,pass_zero=True,fs = fs)
    dftCoeff1 = np.fft.fft(h1)
    dftCoeff2 = np.fft.fft(h2)
    magnitudeCoeff1 = np.abs(dftCoeff1)
    magnitudeCoeff2 = np.abs(dftCoeff2)
    fig = plt.figure()
    fig.add_subplot(311)
    plt.title(window+' filter')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude: LPF')
    plt.plot(np.arange(0,fs,fs/numTaps),magnitudeCoeff1)
    fig.add_subplot(312)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude: BPF')
    plt.plot(np.arange(0,fs,fs/numTaps),magnitudeCoeff2)
    filteredOp1 = np.convolve(ecgNoisy,h1)
    #filteredSignal = np.convolve(filteredOp1,h2)[0:N]
    f1 = signal.filtfilt(h1,1,ecgNoisy)
    filteredSignal = signal.filtfilt(h2,1,f1)
    fig.add_subplot(313)
    plt.xlabel('Time')
    plt.ylabel('Amplitude: Reconstructed Signal')
    plt.plot(ts,filteredSignal)
    ms = (1/N)*np.sum(ecg**2)
    msd = (1/N)*np.sum((filteredSignal - ecg)** 2)
    prd = ((msd/ms)**0.5)*100
    return prd


ecg = scipy.io.loadmat('givenECG3.mat')['givenECG3'].squeeze()
fs = 360
N = ecg.shape[0]
ts = np.arange(0,N*1/fs,1/fs)
contFreq = np.arange(0,fs,fs/N)
fig = plt.figure()
fig.add_subplot(211)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.plot(ts,ecg)
A = 20
bWanderNoise = A*np.sin(2*np.pi*np.random.randn()*ts)
#bWanderNoise = A*np.sin(2*np.pi*1*ts)
powerLineNoise = A*np.sin(2*np.pi*50*ts)
ecgNoisy = ecg + bWanderNoise + powerLineNoise
fig.add_subplot(212)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.plot(ts,ecgNoisy)
prdHamming = firFilter('hamming',N,ecg,ts,fs,ecgNoisy)
prdHanning = firFilter('hann',N,ecg,ts,fs,ecgNoisy)
prdBartlet = firFilter('bartlett',N,ecg,ts,fs,ecgNoisy)

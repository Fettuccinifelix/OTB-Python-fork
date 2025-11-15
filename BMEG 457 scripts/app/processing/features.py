# RMS, MAV, ZC, WL, mean/variance, EMG feature sets.
import numpy as np

def rms(data):
    return np.sqrt(np.mean(data**2, axis=1, keepdims=True))

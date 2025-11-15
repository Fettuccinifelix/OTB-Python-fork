#FFT, STFT, wavelets, Hilbert envelope, etc.
import numpy as np

def fft_transform(data):
    return np.abs(np.fft.rfft(data, axis=1))

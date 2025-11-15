#low-pass, high-pass, notch, Butterworth, FIR, etc.

from scipy.signal import butter, filtfilt

def butter_bandpass(data, low, high, fs, order=4):
    b, a = butter(order, [low/fs*2, high/fs*2], btype="band")
    return filtfilt(b, a, data)

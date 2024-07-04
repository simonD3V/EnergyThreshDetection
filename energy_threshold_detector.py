from scipy.fft import fft
import numpy as np

def freq_max(idx, c, thresh):
    i = [i for i, v in zip(idx, c) if v > thresh]
    return i[0]


class EnergyThresholdDetector:

    def __init__(self, sr, thresholds): 
        self.sr = sr
        self.thresholds = thresholds
    
    def __call__(self, y):
        """
        *** input
        * y: discrete signal

        *** output
        frequency correponding to the maximum energy threshold 
        """

        n = len(y)
        duration = n / self.sr

        # Discrete fast fourier transform
        yf = fft(y)
        spectrum = abs(yf)[:(n // 2)]
        idx = np.array(range(len(spectrum))) * self.sr / n

        # Cumulated sum of energy
        feat = np.sqrt(spectrum)
        c = np.cumsum(feat) / sum(feat)
        
        return [freq_max(idx, c, t) for t in self.thresholds]
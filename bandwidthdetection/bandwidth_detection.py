import numpy as np
import librosa
from scipy.fft import fft


def freq_max(idx, c, thresh):
    i = [i for i, v in zip(idx, c) if v > thresh]
    return i[0]


class BandwidthDetector:

    def __init__(self, sr = 16000, thresholds = [0.97]): 
        self.sr = sr
        self.thresholds = thresholds
    
    def __call__(self, medianame, uem=[]):
        """
        *** input
        * medianame: path to the media to be processed
        * uem: list of tuples (start, stop) indicating the intervals to be analysed (in seconds) 
        
        *** output
        frequencies correponding to the maximum energy threshold for each uem 
        """

        # Load signal
        y, sr = librosa.load(medianame, sr=self.sr)

        if len(uem) == 0 :
            uem = [(0, len(y))]

        res = []

        # Loop on UEM
        for (start, stop) in uem :
        
            # Discrete fast fourier transform
            yf = fft(y[start * sr:stop * sr])
            n = len(y[start * sr:stop * sr])
            
            spectrum = abs(yf)[:(n // 2)]
            idx = np.array(range(len(spectrum))) * self.sr / n
    
            # Cumulated sum of energy
            feat = np.sqrt(spectrum)
            c = np.cumsum(feat) / sum(feat)
            frequencies = [freq_max(idx, c, t) for t in self.thresholds]

            res.append({
                "start":start, 
                "stop":stop, 
                "frequencies":[tup for tup in zip(self.thresholds, frequencies)]
            })
            
        if len(res) == 1:
            res = res[0]
        
        return res
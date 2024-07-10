import numpy as np
from scipy.io import wavfile
from scipy.fft import fft


def freq_max(idx, c, thresh):
    i = [i for i, v in zip(idx, c) if v > thresh]
    return i[0]


class BandwidthEstimator:

    def __init__(self, thresholds = [0.97]): 
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
        sr, y = wavfile.read(medianame)

        if len(uem) == 0 :
            uem = [(0, len(y)/sr)]

        res = []

        # Loop on UEM
        for (start, stop) in uem :
        
            # Discrete fast fourier transform
            _y = y[int(start * sr):int(stop * sr)]
            yf = fft(_y)
            n = len(_y)
            
            spectrum = abs(yf)[:(n // 2)]
            idx = np.array(range(len(spectrum))) * sr / n
    
            # Cumulated sum of energy
            feat = np.sqrt(spectrum)
            c = np.cumsum(feat) / sum(feat)
            frequencies = [freq_max(idx, c, t) for t in self.thresholds]

            res.append({
                "start":int(start * sr), 
                "stop":int(stop * sr),
                "sampling rate":sr,
                "frequencies":[tup for tup in zip(self.thresholds, frequencies)]
            })
            
        if len(res) == 1:
            res = res[0]
        
        return res
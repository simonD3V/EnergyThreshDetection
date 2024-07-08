import unittest

import numpy as np
import librosa
from bandwidthdetection import BandwidthDetector


class TestBandwidthDetection(unittest.TestCase):
    
    def test_init(self):
        BandwidthDetector()

    def test_execution(self):
        medianame = "./audiofiles/poeme_full.wav"
        etd = BandwidthDetector()
        etd(medianame)

    def test_damaged_thresh(self):
        thresh = 0.99
        damaged_freq = 5885.3
        
        medianame = "./audiofiles/poeme_damaged.wav"
        
        bwd = BandwidthDetector(
            thresholds=[thresh]
        )
        
        output = bwd(medianame, uem=[(2, 12)])
        res = output["frequencies"][0]
        
        np.testing.assert_almost_equal(
            res[1],
            damaged_freq,
            decimal=2,
            err_msg="Frequencies are not equal (thresh : %f)" % thresh
        )



# Run tests
if __name__ == '__main__':
    unittest.main()

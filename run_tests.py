import unittest

import numpy as np
import librosa
from energy_threshold_detector import EnergyThresholdDetector

class TestEnergyThreshDetection(unittest.TestCase):
    
    def test_init(self):
        EnergyThresholdDetector()

    def test_execution(self):
        medianame = "./audiofiles/poeme_full.wav"
        etd = EnergyThresholdDetector()
        etd(medianame)

    def test_damaged_thresh(self):
        thresh = 0.99
        damaged_freq = 5884.1
        
        medianame = "./audiofiles/poeme_damaged.wav"
        
        etd = EnergyThresholdDetector(
            sr=16000, 
            thresholds=[thresh]
        )
        
        output = etd(medianame, uem=[(2, 12)])
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

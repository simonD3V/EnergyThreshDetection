import unittest

import numpy as np
import librosa
from energy_threshold_detector import EnergyThresholdDetector

class TestEnergyThreshDetection(unittest.TestCase):
    
    def test_init(self):
        EnergyThresholdDetector()

    def test_execution(self):
        y_full, sr = librosa.load("./audiofiles/poeme_full.wav", sr=16000)
        etd = EnergyThresholdDetector(
                sr=sr, 
                thresholds=[0.99]
        )
        etd(y_full)

    def test_damaged_thresh(self):
        thresh = 0.99
        damaged_freq = 5884.1
        
        y_damaged, sr = librosa.load("./audiofiles/poeme_damaged.wav", sr=16000)
        
        # 10s selection
        y_damaged = y_damaged[sr*2:sr*12]

        etd = EnergyThresholdDetector(
                sr=sr, 
                thresholds=[thresh]
        )
        res = etd(y_damaged)
        np.testing.assert_almost_equal(
                res[0],
                damaged_freq,
                decimal=2,
                err_msg="Frequencies are not equal (thresh : %f)" % thresh
        )



# Run tests
if __name__ == '__main__':
    unittest.main()

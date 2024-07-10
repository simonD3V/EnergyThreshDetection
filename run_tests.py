import unittest

import numpy as np
from bandwidthestimation import BandwidthEstimator


class TestBandwidthEstimation(unittest.TestCase):
    
    def test_init(self):
        BandwidthEstimator()

    def test_execution(self):
        medianame = "./audiofiles/poeme_full.wav"
        bwe = BandwidthEstimator()
        bwe(medianame)

    def test_damaged_thresh(self):
        thresh = 0.99
        damaged_freq = 5885.3
        
        medianame = "./audiofiles/poeme_damaged.wav"
        
        bwe = BandwidthEstimator(
            thresholds=[thresh]
        )
        
        output = bwe(medianame, uem=[(2, 12)])
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

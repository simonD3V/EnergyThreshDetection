# :signal_strength: BandwidthEstimation

Signal processing tool to estimate the maximum energy threshold of one or more audio files. 

Energy above a certain threshold may be lost due to compression manipulations (typically occurs when converting wav :arrow_right: mp3 :arrow_right: wav). This loss can be easily identified for a given sampling rate by examining the maximum frequency obtained for a percentage of the signal energy.  

* Example of _damaged_ signal :

![Damaged signal (10s long excerpt) ](/images/sig.png)
![Corresponding spectrogram (10s long excerpt) ](/images/spectrogram.png)

## PIP installation (in progress)
```bash 
$ virtualenv -p python3 env
$ source env/bin/activate

# install framework and dependencies
$ pip install bandwidthestimation
```

### Audio files from LibriVox
["Demain dès l'aube" (V. HUGO, 1856) read by __Ezwa__.](https://librivox.org/compilation-de-poemes-007-by-various)


from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Filter requirements.
order = 6
fs = 25.0       # sample rate, Hz
cutoff = 2.5  # desired cutoff frequency of the Low-pass filter, Hz

#Clean the signal through a low-pass filter
#To get an high-pass filter select btype='high'  properly changing the cutoff freq.

def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False) 
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order)
    y = lfilter(b, a, data)
    return y

#Unfortunately butter accepts an N-dim array as an input
#Therefore you can't give in input the entire img_collection to butter_low_filter()

lowpass_signal = butter_lowpass_filter(img_collection_reduced[:, 5, 7], cutoff, fs, order) #eg. of a particular signal filtering

plt.plot(lowpass_signal[0:100])
plt.show()

import numpy as np

def butterworth_order(fc, fs):
    return max(1, int(np.ceil(np.log10(0.1)/np.log10(fc/(fs/2)))))

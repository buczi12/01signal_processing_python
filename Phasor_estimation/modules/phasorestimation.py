from scipy import signal
import numpy as np
from math import pi as pi


def full_cycle(source, f_s, fn):
    freqs = [i + 1 for i in range(int(f_s/fn))]
    # real part coeffs
    re = [(np.exp(freq * 2j * pi / (f_s/fn)) * np.sqrt(2) / (f_s/fn)).real for freq in freqs]
    # imag part coeffs
    im = [(np.exp(freq * 2j * pi / (f_s/fn)) * np.sqrt(2) / (f_s/fn)).imag for freq in freqs]

    # filtering - real and imag values estimation
    real = signal.lfilter(re, [1], source)
    imag = signal.lfilter(im, [1], source)

    # magnitude estimation
    mag = abs(real + imag*1j)
    # phase estimation
    pha = np.arctan2(imag, real)

    return mag, pha


def half_cycle(source, f_s, fn):
    freqs = [2 * i for i in range(int(f_s/2/fn))]
    # real part coeffs
    re = [(2 * np.exp(freq * 1j * pi / (f_s/fn)) * np.sqrt(2) / (f_s/fn)).real for freq in freqs]
    # imag part coeffs
    im = [(2 * np.exp(freq * 1j * pi / (f_s/fn)) * np.sqrt(2) / (f_s/fn)).imag for freq in freqs]

    # filtering - real and imag values estimation
    real = signal.lfilter(re, [1], source)
    imag = signal.lfilter(im, [1], source)

    # magnitude estimation
    mag = abs(real + imag*1j)
    # phase estimation
    pha = np.arctan2(imag, real)

    return mag, pha


# for testing purposes
if __name__ == '__main__':
    print('Test message')

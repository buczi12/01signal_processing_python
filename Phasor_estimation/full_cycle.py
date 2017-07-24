# This script aim is to present phasor estimation algorithm used in power system protection
# estimation is based on DFT calculated only for base frequency (50Hz in power system)
# the estimation result is RMS value and phase of sinusoidal signal in time
from math import pi as pi
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# functions definitions

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
    pha = np.arctan(imag/real)

    return mag, pha


# Test data generation
# Electrical system parameters
f1 = 50                                           # [Hz]
A = 110                                           # [kV]
# sampling frequency
fs = 5e3                                          # [Hz]
t = np.arange(0, 1.5/f1, 1/fs)                    # [s]
phi0 = 0                                          # [rad]
# signal generation
sig = A * np.sin(2 * pi * f1 * t + phi0)

# choose estimation method
magnitude, phase = full_cycle(sig, fs, f1)
# theoretical RMS value for visualization
rms = [A/np.sqrt(2) for k in range(len(t))]

# Signals plots
f, axarr = plt.subplots(2, sharex=True)

plot1, = axarr[0].plot(1e3 * t, sig, label="Original signal")
plot2, = axarr[0].plot(1e3 * t, magnitude, label="Estimated RMS value")
plot3, = axarr[0].plot(1e3 * t, rms, 'r--', label="Theoretical RMS value")
axarr[0].set_title('Full cycle magnitude & phase estimation - 110kV sinusoid')
axarr[0].set_ylabel("Voltage [kV]")
axarr[0].legend(handles=[plot1, plot2, plot3], loc=4)
axarr[0].grid()
axarr[0].axis([0, 1e3 * 1.5/f1, -115, 115])


axarr[1].plot(1e3 * t, phase)
axarr[1].set_ylabel("Phase [rad]")
axarr[1].grid()
plt.xlabel("time [ms]")
plt.show()


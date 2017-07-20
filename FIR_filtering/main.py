# python training - FIR filtering sinusoidal signal with noise
import matplotlib.pyplot as plt
from scipy import signal
from math import pi
import numpy as np

# simulation parameters
fs = 5e3                                         # [Hz]
# sinusoidal signals parameters
freq1 = 50                                        # [Hz]
freq2 = 500                                       # [Hz]

# data generation - 5 periods of signal 1
t = np.arange(0, 5/freq1, 1/fs)
y = np.sin(2 * pi * freq1 * t) + 0.3 * np.sin(2 * pi * freq2 * t)

# LowPass filter design, 255 taps, 250 Hz cutoff
coeffs = signal.firwin(31, 250, nyq=fs/2)
w, h = signal.freqz(coeffs)

#  filtering
filtered = signal.lfilter(coeffs, 1, y)

# base signal fft calculation
fourier1 = np.fft.fft(y, n=len(y), norm="ortho")
# filtered signal fft calculation
fourier2 = np.fft.fft(filtered, n=len(filtered), norm="ortho")


# base and filtered signals plot
plot1, = plt.plot(t, y, label="Original signal")
plot2, = plt.plot(t, filtered, label="Filtered signal")
plt.legend(handles=[plot1, plot2])
plt.xlabel('Time [s]')
plt.title('Original and filtered signals')
plt.grid()
plt.show()

# digital filter frequency response
plt.title('Filter coefficients')
plt.plot(coeffs, '*')
plt.grid()
plt.show()

# fft plot - original signal
freqs1 = np.fft.fftfreq(len(fourier1), 1/fs)
plt.plot(freqs1, abs(fourier1))
plt.axis([0, 1600, 0, max(abs(fourier1))])
plt.grid()
plt.xlabel('Frequency [Hz]')
plt.title('DFT of the original signal')
plt.show()

# fft plot - filtered signal
freqs2 = np.fft.fftfreq(len(fourier2), 1/fs)
plt.plot(freqs2, abs(fourier2))
plt.axis([0, 1600, 0, max(abs(fourier2))])
plt.grid()
plt.title('DFT of the filtered signal')
plt.xlabel('Frequency [Hz]')
plt.show()


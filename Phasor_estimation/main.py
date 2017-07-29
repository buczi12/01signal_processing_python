# This script aim is to present phasor estimation algorithm used in power system protection
# estimation is based on DFT calculated only for base frequency (50Hz in power system)
# the estimation result is RMS value and phase of sinusoidal signal in time
from math import pi as pi
import numpy as np
import matplotlib.pyplot as plt
from modules import phasorestimation as pe
import matplotlib.style as style

style.use('ggplot')

# Test data generation
# Electrical system parameters
f1 = 50                                           # [Hz]
A = 110 * np.sqrt(2)                              # [kV]
# sampling frequency
fs = 1e3                                          # [Hz]
t = np.arange(0, 2/f1, 1/fs)                    # [s]
phi0 = 0                                          # [rad]
# signal generation
sig = A * np.sin(2 * pi * f1 * t + phi0)

# choose estimation method
magnitude1, phase1 = pe.half_cycle(sig, fs, f1)
magnitude2, phase2 = pe.full_cycle(sig, fs, f1)

# theoretical RMS value for visualization
rms = [A/np.sqrt(2) for k in range(len(t))]

# Signals plots
plt.figure(1)
plt.subplot(211)
plot1, = plt.plot(1e3 * t, sig, label="original signal")
plot3, = plt.plot(1e3 * t, magnitude1, 'g--', label="half-cycle DFT")
plot4, = plt.plot(1e3 * t, magnitude2, 'm--', label="full-cycle DFT")
plot2, = plt.plot(1e3 * t, rms, 'r', label="theoretical RMS value")
plt.legend(handles=[plot1, plot2, plot3, plot4], loc=4)
plt.title("RMS and phase estimation of 110kV sinusoid")
plt.ylabel("Voltage [kV]")
plt.xlabel("time [ms]")
# plt.grid()

plt.subplot(212)
plot1, = plt.plot(1e3 * t, phase1, 'g--', label="half-cycle")
plot2, = plt.plot(1e3 * t, phase2, 'm--', label="full-cycle")
plt.legend(handles=[plot1, plot2], loc=4)
plt.xlabel("time [ms]")
plt.ylabel("Phase [rad]")
# plt.grid()

# fullsize figure - depends on matplotlib backend
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
plt.show()

# Functions for quick circuit analysis calcs
import numpy as np
import matplotlib.pyplot as plt
import math

def IR(current, resistance):
    # Ohms law
    # V = IR
    return current * resistance

def plot_resonance(R, L, C):
    # Displays impedance of RLC circuit
    # at both extreme sides of resonance
    w_resonance = 1.0/math.sqrt(L*C)
    f_neper = R / (2.0 * L)
    damping_factor = f_neper / w_resonance
    f_resonance = w_resonance * math.pi * 2.0
    print('Resonance frequency: %2e Hz' % f_resonance)
    resonance_order_of_mag = math.log(f_resonance, 10)
    f = np.logspace(resonance_order_of_mag - 5, resonance_order_of_mag + 5, 100)

    z = [math.sqrt(R**2 + math.pow(2*math.pi*f_i*L - (1.0/(2*math.pi*f_i*C)), 2)) for f_i in f]

    plt.loglog(f, z)
    plt.show()

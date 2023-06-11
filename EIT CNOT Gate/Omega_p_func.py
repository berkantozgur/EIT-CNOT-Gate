from math import cos, pi
import numpy as np

def Omega_p_func(t, op_max, tau):
    #result = (op_max/2) * (1 - 2*cos((pi * t)/tau)**2)
    result = (op_max * (1 - np.cos((2 * np.pi * t)/tau)))/2
    return result
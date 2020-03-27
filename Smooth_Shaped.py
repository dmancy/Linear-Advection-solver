import numpy as np

#Generation of a smooth signal
def Smooth_Shaped(X, x1, x2, t, a):
    U = [0] * len(X)
    for i, x in enumerate(X):
        if (x1 <= x - a*t <= x2):
            U[i] = 1.0 - 0.5*np.cos(np.pi * (x-a*t) / 10)

        else:
            U[i] = 0.5
    return U

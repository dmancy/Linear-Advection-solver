import numpy as np

def Smooth_Shaped(X, x1, x2):
    U = [0] * len(X)
    for i, x in enumerate(X):
        if (x1 <= x <= x2):
            U[i] = 1.0 - 0.5*np.cos(np.pi * x / 10)

        else:
            U[i] = 0.5
    return U

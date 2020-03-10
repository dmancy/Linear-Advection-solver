import numpy as np

def Triangle_Shaped(X, x1, x2, t, a):
    U = [0] * len(X)
    for i, x in enumerate(X):
        if (x1 <= x - a*t <= x2):
            U[i] = .5 + 0.075 * (x - a*t)

        else:
            U[i] = 0.5
    return U

import numpy as np

def Triangle_Shaped(X, x1, x2):
    U = [0] * len(X)
    for i, x in enumerate(X):
        if (x1 <= x <= x2):
            U[i] = 0.5 + 0.075*x

        else:
            U[i] = 0.5
    return U

import numpy as np

class Grid:
    """Define Grid"""

    def __init__(self, x1, x2, N):

        self.x1 = x1
        self.x2 = x2
        self.N  = N
        self.grid = np.linspace(x1, x2, N)
        self.delta_x = [self.grid[i+1] - self.grid[i] for i in range(len(self.grid -1))] 

import matplotlib.pyplot as plt
import numpy as np
from Triangle_Shaped import Triangle_Shaped
from Grid import Grid
from CIR import CIR_scheme
from Lax_Wendroff import Lax_Wendroff_scheme



#Grid generation
faces = np.linspace(-10, 300, 100)

grid = Grid(faces)


#Triangle-shaped signal
U = Triangle_Shaped(grid.cell_position, 0, 20) 

plt.plot(grid.cell_position,U)

U_origin = U

a = 2
Courant_number = .6


U_final = Lax_Wendroff_scheme(U_origin, grid, 0.6, a, 0, 100)
plt.plot(grid.cell_position, U_final, "+")


U_final = Lax_Wendroff_scheme(U_origin, grid, 1, a, 0, 100)
plt.plot(grid.cell_position, U_final)


plt.show()


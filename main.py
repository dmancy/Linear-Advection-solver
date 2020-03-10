#Python libraries
import matplotlib.pyplot as plt
import numpy as np

#Functions from other files
from Triangle_Shaped import Triangle_Shaped
from Smooth_Shaped import Smooth_Shaped
from Grid import Grid
from CIR import CIR_scheme
from Lax_Wendroff import Lax_Wendroff_scheme



#Grid generation
faces = np.linspace(-5, 250, 256)
print(faces)
grid = Grid(faces)


#Triangle-shaped signal
U = Triangle_Shaped(grid.cell_position, 0, 20) 

#Smooth signal
#U = Smooth_Shaped(grid.cell_position, 0, 20)

#plt.plot(grid.cell_position,U)

U_origin = U

a = 2
Courant_number = 1.02

t_0 = 0
t_final = 100

#Exact solution
faces_offset = [faces[i] - a*t_final for i in range(len(faces))]
grid_offset = Grid(faces_offset)
U_exact = Triangle_Shaped(grid_offset.cell_position, 0 , 20)
plt.plot(grid.cell_position, U_exact, "-")

U_final = CIR_scheme(U_origin, grid, Courant_number, a, t_0, t_final)
plt.plot(grid.cell_position, U_final, "+")


#U_final = Lax_Wendroff_scheme(U_origin, grid, 1, a, 0, 100)
#plt.plot(grid.cell_position, U_final)

plt.grid()
plt.xlabel("Location")
plt.ylabel(r"$u(x,100)$")
plt.legend(["Exact solution", "CIR scheme"])
plt.title(r"Solution of the linear advection equation for $\nu = 1.02$.") 


plt.show()


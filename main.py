#Python libraries
import matplotlib.pyplot as plt
import numpy as np

#Functions from other files
from Triangle_Shaped import Triangle_Shaped
from Smooth_Shaped import Smooth_Shaped
from Grid import Grid
from CIR import CIR_scheme
from Lax_Wendroff import Lax_Wendroff_scheme

def norm_2(U):
    n = len(U)
    norm = 0.0
    for i in range(n):
        norm += U[i]**2

    return (norm/n)**.5


#Grid generation
faces = np.linspace(-21, 260, 282)
grid = Grid(faces)

a = 2
Courant_number = 2
t_0 = 0
t_final = 100

#Triangle-shaped signal
U = Triangle_Shaped(grid.cell_position, 0, 20, t_0, a) 

#Smooth signal
#U = Smooth_Shaped(grid.cell_position, 0, 20)

#plt.plot(grid.cell_position,U)

U_origin = U

#for i in range(len(U_origin)):
#    print(i+1, grid.cell_position[i],  U_origin[i])



#Exact solution
U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, 100, a)
#plt.plot(grid.cell_position, U_exact, "-")

#U_final = CIR_scheme(U_origin, grid, Courant_number, a, t_0, t_final)
#plt.plot(grid.cell_position, U_final, "+")

#Stability limit

#for C = 0.8
plt.figure()
U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, 100, a)
plt.plot(grid.cell_position, U_exact, "-")
U_final, five_steps = CIR_scheme(U_origin, grid, .8, a, t_0, t_final)
plt.plot(grid.cell_position, U_final, "+")

plt.grid()
plt.xlabel("Location")
plt.ylabel(r"$u(x,100)$")
plt.legend(["Exact solution", "CIR scheme"])
plt.title(r"Solution of the linear advection equation for $C = 0.8$.") 


#first 5 iterations 
fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]
for i in range(5):
    U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, five_steps[5][i], a)
    ax_list[i].plot(grid.cell_position, U_exact, "-")
    ax_list[i].plot(grid.cell_position, five_steps[i], '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,{})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    ax_list[i].set_ylim(0.426125, 2.0513749999999997)

fig.suptitle(r"Five first time steps for $C = 0.8$.") 

fig.tight_layout()

#for C = 1.2
plt.figure()
U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, 100, a)
plt.plot(grid.cell_position, U_exact, "-")
U_final, five_steps = CIR_scheme(U_origin, grid, 1.02, a, t_0, t_final)
plt.plot(grid.cell_position, U_final, "+")

plt.grid()
plt.xlabel("Location")
plt.ylabel(r"$u(x,100)$")
plt.legend(["Exact solution", "CIR scheme"])
plt.title(r"Solution of the linear advection equation for $C = 1.02$.") 

#first 5 iterations 
fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]
for i in range(5):
    U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, five_steps[5][i], a)
    ax_list[i].plot(grid.cell_position, U_exact, "-")
    ax_list[i].plot(grid.cell_position, five_steps[i], '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,{})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    ax_list[i].set_ylim(0.426125, 2.0513749999999997)

fig.suptitle(r"Five first time steps for $C = 1.02$.") 

fig.tight_layout()


#for C = 2.0
plt.figure()
U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, 100, a)
plt.plot(grid.cell_position, U_exact, "-")
U_final, five_steps = CIR_scheme(U_origin, grid, 2.0, a, t_0, t_final)
plt.plot(grid.cell_position, U_final, "+")

plt.grid()
plt.xlabel("Location")
plt.ylabel(r"$u(x,100)$")
plt.legend(["Exact solution", "CIR scheme"])
plt.title(r"Solution of the linear advection equation for $C = 2.0$.") 

#first 5 iterations 
fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]
for i in range(5):
    U_exact = Triangle_Shaped(grid.cell_position, 0 , 20, five_steps[5][i], a)
    ax_list[i].plot(grid.cell_position, U_exact, "-")
    ax_list[i].plot(grid.cell_position, five_steps[i], '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,{})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    ax_list[i].set_ylim(0.426125, 2.0513749999999997)

fig.suptitle(r"Five first time steps for $C = 2.0$.") 
fig.tight_layout()

#U_final = Lax_Wendroff_scheme(U_origin, grid, 1, a, 0, 100)
#plt.plot(grid.cell_position, U_final)


#Study of convergence
face_list = [np.arange(-10, 260, 0.4/i) for i in range(1,6)]
grid_list = [Grid(face_list[i]) for i in range(5)]



fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]

norm_list = []

for i in range(5):
    U_origin = Triangle_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_exact = Triangle_Shaped(grid_list[i].cell_position, 0 , 20, t_final, a)
    U_final, five_steps = CIR_scheme(U_origin, grid_list[i], .9, a, t_0, t_final)

    norm_list.append(np.log(norm_2(U_final)))

    ax_list[i].plot(grid_list[i].cell_position, U_exact, "-")
    ax_list[i].plot(grid_list[i].cell_position, U_final, '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,100)$")
    ax_list[i].set_xlim(190,230)
    ax_list[i].set_xlim(190,230)
    ax_list[i].title.set_text(r"$\Delta x = {0:.3g}$".format(grid_list[i].cell_length[0]))

fig.tight_layout()


#Global order of convergence
log_delta_x = [np.log(grid_list[i].cell_length[0]) for i in range(5)]

plt.figure()

plt.plot(log_delta_x, norm_list, "-+")




plt.show()



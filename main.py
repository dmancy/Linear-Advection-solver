#Python libraries
import matplotlib.pyplot as plt
import numpy as np

#Functions from other files
from Triangle_Shaped import Triangle_Shaped
from Smooth_Shaped import Smooth_Shaped
from Grid import Grid
from CIR import CIR_scheme
from Lax_Wendroff import Lax_Wendroff_scheme
from norm_2 import norm_2



#Definition of the faces
faces = np.linspace(-10, 260, 676)

#Grid generation
grid = Grid(faces)

#Advection coefficient
a = 2

#Courant number
Courant_number = 1

#Time settings
t_0 = 0
t_final = 100

####################
#Initial conditions#
####################
#Triangle-shaped signal
U_triangle_init = Triangle_Shaped(grid.cell_position, 0, 20, t_0, a) 

#Smooth signal
U_smooth_init = Smooth_Shaped(grid.cell_position, 0, 20, t_0, a)


#Exact solutions
U_triangle_exact = Triangle_Shaped(grid.cell_position, 0 , 20, t_final, a)
U_smooth_exact = Smooth_Shaped(grid.cell_position, 0 , 20, t_final, a)



#####################
#1-1 Stability limit#
#####################


##############################
#Triangle shaped signal

############
#For C = 0.8
plt.figure()

U_final, five_steps = CIR_scheme(U_triangle_init, grid, .8, a, t_0, 100)

#Plot
plt.plot(grid.cell_position, U_triangle_exact, "-")
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
    ax_list[i].set_ylabel(r"$u(x,{:.3})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    ax_list[i].set_ylim(0.426125, 2.08)

fig.suptitle(r"Five first time steps for $C = 0.8$.") 

fig.tight_layout(rect=[0, 0.03, 1, 0.95])

############
#For C = 1.2
plt.figure()

U_final, five_steps = CIR_scheme(U_triangle_init, grid, 1.02, a, t_0, t_final)

#plot
plt.grid()
plt.plot(grid.cell_position, U_triangle_exact, "-")
plt.plot(grid.cell_position, U_final, "+")
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
    ax_list[i].set_ylabel(r"$u(x,{:.3})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    ax_list[i].set_ylim(0.426125, 2.08)

fig.suptitle(r"Five first time steps for $C = 1.02$.") 
fig.tight_layout(rect=[0, 0.03, 1, 0.95])


############
#For C = 2.0
plt.figure()
U_final, five_steps = CIR_scheme(U_triangle_init, grid, 2.0, a, t_0, t_final)

plt.grid()
plt.plot(grid.cell_position, U_triangle_exact, "-")
plt.plot(grid.cell_position, U_final, "+")
plt.xlabel("Location")
plt.ylabel(r"$u(x,100)$")
plt.legend(["Exact solution", "CIR scheme"])
plt.ylim(0.426125, 2.1)
plt.xlim(left=150)
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
    ax_list[i].set_ylabel(r"$u(x,{:.3})$".format(five_steps[5][i]))
    ax_list[i].set_xlim(-2.5,35)
    #ax_list[i].set_ylim(0.426125, 2.08)

fig.suptitle(r"Five first time steps for $C = 2.0$.") 
fig.tight_layout(rect=[0, 0.03, 1, 0.95])



##########################
#1-2 Study of convergence#
##########################

#Generation of the meshes
face_list = [np.arange(-10, 260, 0.4/2**i) for i in range(1,5)]
grid_list = [Grid(face_list[i]) for i in range(4)]


Courant_number = 0.9

##########################
#CIR Triangle-shaped signal

fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]

for i in range(4):
    U_origin = Triangle_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_exact = Triangle_Shaped(grid_list[i].cell_position, 0 , 20, t_final, a)
    U_final, five_steps = CIR_scheme(U_origin, grid_list[i], Courant_number, a, t_0, t_final)


    ax_list[i].plot(grid_list[i].cell_position, U_exact, "-")
    ax_list[i].plot(grid_list[i].cell_position, U_final, '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,100)$")
    ax_list[i].set_xlim(190,230)
    ax_list[i].set_xlim(190,230)
    ax_list[i].title.set_text(r"$\Delta x = {0:.3g}$".format(grid_list[i].cell_length[0]))

fig.tight_layout(rect=[0, 0.03, 1, 0.95])

##########################
#Lax-Wendroff Triangle-shaped signal

fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]

for i in range(4):
    U_origin = Triangle_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_exact = Triangle_Shaped(grid_list[i].cell_position, 0 , 20, t_final, a)
    U_final, five_steps = Lax_Wendroff_scheme(U_origin, grid_list[i], Courant_number, a, t_0, t_final)

    ax_list[i].plot(grid_list[i].cell_position, U_exact, "-")
    ax_list[i].plot(grid_list[i].cell_position, U_final, '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,100)$")
    ax_list[i].set_xlim(190,230)
    ax_list[i].set_xlim(190,230)
    ax_list[i].title.set_text(r"$\Delta x = {0:.3g}$".format(grid_list[i].cell_length[0]))

fig.tight_layout(rect=[0, 0.03, 1, 0.95])

##########################
#Lax-Wendroff Smooth signal

fig = plt.figure(figsize = (9,5.5))
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)

ax_list = [ax1, ax2, ax3, ax4, ax5]

for i in range(4):
    U_origin = Smooth_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_exact = Smooth_Shaped(grid_list[i].cell_position, 0 , 20, t_final, a)
    U_final, five_steps = Lax_Wendroff_scheme(U_origin, grid_list[i], Courant_number, a, t_0, t_final)

    ax_list[i].plot(grid_list[i].cell_position, U_exact, "-")
    ax_list[i].plot(grid_list[i].cell_position, U_final, '+')
    ax_list[i].grid()
    ax_list[i].set_xlabel("Location")
    ax_list[i].set_ylabel(r"$u(x,100)$")
    ax_list[i].set_xlim(190,230)
    ax_list[i].set_xlim(190,230)
    ax_list[i].title.set_text(r"$\Delta x = {0:.3g}$".format(grid_list[i].cell_length[0]))

fig.tight_layout(rect=[0, 0.03, 1, 0.95])



##############################
#1-3 Global order of accuracy#
##############################

##############################
#CIR triangle

norm_list = []
for i in range(4):
    U_origin = Triangle_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_final, five_steps = CIR_scheme(U_origin, grid_list[i], .9, a, t_0, t_final)
    U_exact = Triangle_Shaped(grid_list[i].cell_position, 0 , 20, 100, a)
    e = [U_exact[k] - U_final[k] for k in range(len(grid_list[i].cell_position))] 
    norm_list.append(norm_2(e))


log_delta_x = [1/(grid_list[i].cell_length[0]) for i in range(4)]

#plot
plt.figure()
plt.ylabel(r"$||e||_2$")
plt.xlabel(r"$\frac{1}{\Delta x}$")
plt.title("CIR Triangle-shaped signal")

plt.loglog(log_delta_x, norm_list, "-+")

#Computation of the slope
slope = np.log(norm_list[-1]/norm_list[0])/np.log(grid_list[-1].cell_length[0]/grid_list[0].cell_length[0])
print("CIR Triangle-shaped signal, Slope = ", slope)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])


##############################
#CIR Smooth signal

norm_list = []
for i in range(4):
    U_origin = Smooth_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_final, five_steps = CIR_scheme(U_origin, grid_list[i], .9, a, t_0, t_final)
    U_exact = Smooth_Shaped(grid_list[i].cell_position, 0 , 20, 100, a)
    e = [U_exact[k] - U_final[k] for k in range(len(grid_list[i].cell_position))] 
    norm_list.append(norm_2(e))


log_delta_x = [1/(grid_list[i].cell_length[0]) for i in range(4)]

#plot
plt.figure()
plt.ylabel(r"$||e||_2$")
plt.xlabel(r"$\frac{1}{\Delta x}$")
plt.title("CIR Smooth signal")

plt.loglog(log_delta_x, norm_list, "-+")

#Computation of the slope
slope = np.log(norm_list[-1]/norm_list[0])/np.log(grid_list[-1].cell_length[0]/grid_list[0].cell_length[0])
print("CIR Smooth signal, Slope = ", slope)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])


##############################
#Lax-Wendroff triangle

norm_list = []
for i in range(4):
    U_origin = Triangle_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_final, five_steps = Lax_Wendroff_scheme(U_origin, grid_list[i], .9, a, t_0, t_final)
    U_exact = Triangle_Shaped(grid_list[i].cell_position, 0 , 20, 100, a)
    e = [U_exact[k] - U_final[k] for k in range(len(grid_list[i].cell_position))] 
    norm_list.append(norm_2(e))


log_delta_x = [1/(grid_list[i].cell_length[0]) for i in range(4)]

#plot
plt.figure()
plt.ylabel(r"$||e||_2$")
plt.xlabel(r"$\frac{1}{\Delta x}$")
plt.title("Lax-Wendroff Triangle-shaped signal")

plt.loglog(log_delta_x, norm_list, "-+")

#Computation of the slope
slope = np.log(norm_list[-1]/norm_list[0])/np.log(grid_list[-1].cell_length[0]/grid_list[0].cell_length[0])
print("Lax-Wendroff Triangle-shaped signal, Slope = ", slope)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])


##############################
#Lax-Wendroff Smooth signal

norm_list = []
for i in range(4):
    U_origin = Smooth_Shaped(grid_list[i].cell_position, 0, 20, t_0, a) 
    U_final, five_steps = Lax_Wendroff_scheme(U_origin, grid_list[i], .9, a, t_0, t_final)
    U_exact = Smooth_Shaped(grid_list[i].cell_position, 0 , 20, 100, a)
    e = [U_exact[k] - U_final[k] for k in range(len(grid_list[i].cell_position))] 
    norm_list.append(norm_2(e))


log_delta_x = [1/(grid_list[i].cell_length[0]) for i in range(4)]

#plot
plt.figure()
plt.ylabel(r"$||e||_2$")
plt.xlabel(r"$\frac{1}{\Delta x}$")
plt.title("Lax-Wendroff Smooth signal")

plt.loglog(log_delta_x, norm_list, "-+")

#Computation of the slope
slope = np.log(norm_list[-1]/norm_list[0])/np.log(grid_list[-1].cell_length[0]/grid_list[0].cell_length[0])
print("Lax-Wendroff Smooth signal, Slope = ", slope)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])



#Plot of all the Figures
plt.show()



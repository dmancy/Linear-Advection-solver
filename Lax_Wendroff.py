import numpy as np

def Lax_Wendroff_scheme(U_init, Grid, Courant_number, advection_coefficient, t0, t_final):

    #Copy of U_init
    U = np.zeros(len(U_init))
    for i in range(len(U)):
        U[i] = U_init[i]

    U_new = np.zeros(len(U_init))

    t = t0

    max_delta_x = 0
    for delta_x in Grid.cell_length:
        if delta_x > max_delta_x:
            max_delta_x = delta_x

    delta_t = Courant_number * max_delta_x/ advection_coefficient

    step = 0
    five_first_steps = [[0] * len(U) for i in range(5)]
    five_first_steps += [[0] * 5]

    while t < t_final:

        t += delta_t
        if ( t > t_final):
            delta_t -= t - t_final

        for i, cell in enumerate(Grid.cell_position):
            #Lax-Wendroff scheme
            if 0 < i < len(Grid.cell_position)-1:
                U_new[i] = U[i] - delta_t * advection_coefficient / (2 * Grid.cell_length[i]) * (U[(i+1) % len(U)] - U[i-1])  + (delta_t * advection_coefficient /  Grid.cell_length[i])**2  / 2 * (U[(i+1) % len(U)] - 2*U[i] + U[i-1]) 
            elif i == 0:
                U_new[i] = U[i] - delta_t * advection_coefficient / (2 * Grid.cell_length[i]) * (U[(i+1)] - U[i])  + (delta_t * advection_coefficient /  Grid.cell_length[i])**2  / 2 * (U[i+1] - 2*U[i] + U[i]) 
            else:
                U_new[i] = U[i] - delta_t * advection_coefficient / (2 * Grid.cell_length[i]) * (U[(i)] - U[i])  + (delta_t * advection_coefficient /  Grid.cell_length[i])**2  / 2 * (U[i] - 2*U[i] + U[i]) 


        for i in range(len(U)):
            U[i] = U_new[i]
            if step < 5:
                five_first_steps[step][i] = U_new[i] 

        if step < 5:
            five_first_steps[5][step] = t

        step+=1



    return U, five_first_steps

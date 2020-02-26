import numpy as np

def CIR_scheme(U_init, Grid, Courant_number, advection_coefficient, t0, t_final):

    U = np.copy(U_init)
    U_new = np.zeros(len(U_init))

    t = t0

    max_delta_x = 0
    for delta_x in Grid.cell_length:
        if delta_x > max_delta_x:
            max_delta_x = delta_x

    delta_t = Courant_number * max_delta_x/ advection_coefficient

    while t <= t_final:

        for i, cell in enumerate(Grid.cell_position):
            #CIR scheme
            U_new[i] = U[i] - delta_t * advection_coefficient / Grid.cell_length[i] * (U[i] - U[i-1])

        for i in range(len(U)):
            U[i] = U_new[i]

        if (t == t_final):
            break

        t += delta_t

        if ( t > t_final):
            delta_t -= t + delta_t - t_final


    return U

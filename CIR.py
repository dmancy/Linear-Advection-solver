import numpy as np

def CIR_scheme(U_init, Grid, Courant_number, advection_coefficient, t0, t_final):

    #Copy of U_init
    U = np.copy(U_init)

    U_new = np.zeros(len(U))

    t = t0

    min_delta_x = Grid.cell_length[0]
    for delta_x in Grid.cell_length:
        if delta_x < min_delta_x:
            min_delta_x = delta_x

    delta_t = Courant_number * min_delta_x/ advection_coefficient

    step = 0
    five_first_steps = [[0] * len(U) for i in range(5)]
    five_first_steps += [[0] * 5]

    while t < t_final:

        t += delta_t
        if ( t > t_final):
            delta_t -= t - t_final
            break

        for i, cell in enumerate(Grid.cell_position):
            #CIR scheme
            if i == 0:
                U_new[i] = U[i] - delta_t * advection_coefficient / Grid.cell_length[i] * (U[i] - U[i])
            else :
                U_new[i] = U[i] - delta_t * advection_coefficient / Grid.cell_length[i] * (U[i] - U[i-1])

        for i in range(len(U)):
            U[i] = U_new[i]
            if step < 5:
                five_first_steps[step][i] = U_new[i] 

        if step < 5:
            five_first_steps[5][step] = t

        step+=1

    return U, five_first_steps

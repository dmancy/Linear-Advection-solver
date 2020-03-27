#Compute the second norm of a vector normalized by its size
def norm_2(U):
    n = len(U)
    norm = 0.0
    for i in range(n):
        norm += U[i]**2

    return (norm/n)**.5

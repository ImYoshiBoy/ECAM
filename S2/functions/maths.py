import numpy as np
def taylor_exp(x, x0, order):
    expansion = 0
    for n in range(order+1):
        expansion += (x - x0)**n / np.math.factorial(n)
    return expansion
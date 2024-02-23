import matplotlib.pyplot as plt

import numpy as np

#ex1

# x = np.linspace(-np.pi / 2, np.pi / 2, 100)
# y = np.sin(x)

# plt.plot(x, y)

# plt.grid()
# plt.title("sin(x) bewteen -pi/2 and pi/2")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.show()

#ex 2
x = np.linspace(-2, 3, 200)
y = np.exp(x)
plt.grid()
plt.plot(x, y, label='e**x')

def taylor_exp(x, x0, order):
    expansion = 0
    for n in range(order+1):
        expansion += (x - x0)**n / np.math.factorial(n)
    return expansion

x1=np.linspace(-2, 3, 200)
y1=taylor_exp(x1, 0, 3)
plt.plot(x1, y1)

plt.show()



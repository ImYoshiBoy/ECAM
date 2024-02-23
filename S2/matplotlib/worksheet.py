import matplotlib.pyplot as plt

import numpy as np

#ex1

x = np.linspace(-np.pi / 2, np.pi / 2, 100)
y = np.sin(x)
# plt.plot(x, y)
# plt.grid()
# plt.title("sin(x) bewteen -pi/2 and pi/2")
# plt.xlabel("x")
# plt.ylabel("sin(x)")


#ex 2
x = np.linspace(-2, 3, 2000)
y = np.exp(x)
plt.grid()
plt.plot(x, y, label='e**x')

def taylor_exp(x, x0, order):
    expansion = 0
    for n in range(order+1):
        expansion += (x - x0)**n / np.math.factorial(n)
    return expansion


for i in range(1, 5):
    x1=np.linspace(-2, 3, 2000)
    y1=taylor_exp(x1, 0, i+1)
    plt.plot(x1, y1, label=f'Taylor expansion of order {i}', ls="--")



plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()



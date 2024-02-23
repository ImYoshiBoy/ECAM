import matplotlib.pyplot as plt

import numpy as np

x = [0, 1, 2, 3, 4, 5, 6]
y = []


for i in x:
    y.append(i**2)

plt.plot(x, y, ls="--", color="red", marker="x", mec="b")
plt.grid()
plt.axis([-1, 7, -5, 40])
plt.xlabel("n")
plt.ylabel("n²")
plt.title("Squarte of the first integers")
plt.show()

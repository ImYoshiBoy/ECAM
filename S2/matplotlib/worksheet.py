import matplotlib.pyplot as plt

import numpy as np

#ex1

x = np.linspace(-np.pi / 2, np.pi / 2, 100)
y = np.sin(x)

plt.plot(x, y)
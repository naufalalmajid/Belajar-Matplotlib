# we can use plot() for plotting, which first parameters is x axis and secondary is y axis
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 8])
y = np.array([8, 9])

plt.plot(x, y)
plt.show()

# in case plotting without line we can use parameter 'o' like plt.plot(x, y, 'o')

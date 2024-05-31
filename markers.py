import numpy as np
import matplotlib.pyplot as plt

y = np.array([2, 2, 5, 5, 2, 8, 8, 9, 9])
plt.plot(y, marker="o")
plt.show()

# in case marker we can use any type of marker, read at marker.txt
# and we can make format (fmt) which writted as(marker line color)
# plt.plot(y, 'o:r')

# for size of marker we can use ms or markersize keyword argument
# for color of the edge of the marker we can use markeredcolor or mec keyword argument
# for color of the inside of the marker we can use markerfacecolor or mfc keyword argument

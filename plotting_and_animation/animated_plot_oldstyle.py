import time
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])
plt.ion()
plt.show()

for i in range(1000):
    y = np.random.random()
    plt.scatter(i, y)
    plt.draw()
    plt.pause(0.01)
    #the following line causes the plot to wait!
    #_ = raw_input("Press [enter] to continue")

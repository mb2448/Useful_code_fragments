import time
import numpy as np
import matplotlib.pyplot as plt

#plt.axis([0, 1000, 0, 1])
plt.ion()
a = plt.imshow(np.random.random((100, 100)))
plt.show()

for i in range(1000):
    q = np.random.random((100, 100))
    a.set_data(q)
    plt.draw()
    plt.pause(0.01)

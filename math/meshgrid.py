import numpy as np
nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)

print(xv)
print(yv)
#xv, yv = meshgrid(x, y, sparse=True)  # make sparse output arrays

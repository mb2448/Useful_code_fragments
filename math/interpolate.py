from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

xvals = np.arange(0, 2*np.pi,.01)
yvals = np.sin(xvals)

f = interpolate.interp1d(xvals, yvals)

xnew = np.arange(1, 5, .3)
ynew = f(xnew)

plt.plot(xvals, yvals, 'r-')
plt.plot(xnew, ynew, 'b.')
plt.show()


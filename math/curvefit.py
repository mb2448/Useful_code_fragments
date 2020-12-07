import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a*np.exp(-b*x) + c

x = np.linspace(0,4,50)
true_vals = [2.5, 1.3, 0.5]
y = func(x, *true_vals)
yn = y + 0.2*np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, yn)

print("True: ", true_vals)
print("Fit Opt: ",popt)
print("Fit Cov: ",pcov)

plt.plot(x, yn, 'k.', label="Noisy")
plt.plot(x, y, label="True")
plt.plot(x, func(x, *popt), label="Fit")
plt.legend()
plt.show()

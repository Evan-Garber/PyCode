import numpy as np
import matplotlib.pyplot as plt
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("displacement vs time")

t = np.linspace(0,10,1000)
A = 10
b = 10
m = 10
k = 100
w = np.sqrt((k / m) - (b / (2 * m))**2)
x = A * np.exp(-b * t / (2 * m)) * np.cos(w * t)
plt.plot(t, x) 
plt.show()

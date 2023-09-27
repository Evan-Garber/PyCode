import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

g = 9.8
m1 = 10
m2 = 10
L1 = 1
L2 = 1
L = L1 + L2

y0 = np.radians([-100, 0, 60, 0])  # initial conditions: [theta1, omega1, theta2, omega2]

t = [0,5]

def f(t, y):
    
    theta1 = y[0]
    omega1 = y[1]
    theta2 = y[2]
    omega2 = y[3]

    dtdt1 = omega1   
    dwdt1 = (-g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2))) / (L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    dtdt2 = omega2   
    dwdt2 = (2 * np.sin(theta1 - theta2) * (omega1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2**2 * L2 * m2 * np.cos(theta1 - theta2))) / (L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))    
    return [dtdt1,dwdt1,dtdt2,dwdt2]

sol = integrate.solve_ivp(f, t, y0, t_eval = np.linspace(t[0],t[1],1000))

y0 = sol.y[0]
y1 = sol.y[1]
y2 = sol.y[2]
y3 = sol.y[3]

# find the x and y coordinates of m1 and m2
x1 = L1 * np.sin(y0);
y1 = - L1 * np.cos(y0);

x2 = x1 + L2 * np.sin(y2);
y2 = y1 - L2 * np.cos(y2);

# plot everything
plt.xlim(-L,L)
plt.ylim(-L,L)

plt.plot(x1,y1, 'r-')
plt.plot(x2,y2, 'b-')

plt.plot(x1[-1],y1[-1],'ro')
plt.plot(x2[-1],y2[-1],'bo')

plt.plot(0,0,'ko')
plt.plot([0, x1[-1]], [0, y1[-1]], 'black')
plt.plot([x1[-1], x2[-1]], [y1[-1], y2[-1]], 'black')
plt.show()
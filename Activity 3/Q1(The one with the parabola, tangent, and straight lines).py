#Reuben Aucamp, ACMREU001

import pylab as plt
import numpy as np

x=np.linspace(-1.5,3,100)
y=-2*x**2+3*x+5
m=-4*1.75+3
y17=-2*1.75**2+3*1.75+5
y2=m*(x-1.75)+y17

plt.plot(x[0:99],y[0:99],'-k')
plt.plot(x[51:100],y2[51:100],'-r')
plt.plot([0,0],[-4,8],'-b')
plt.plot([-1.5,3],[0,0],'-b')
plt.ylabel('y')
plt.xlabel('x')

plt.show()

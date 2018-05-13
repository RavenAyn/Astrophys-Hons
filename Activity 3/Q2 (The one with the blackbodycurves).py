#Reuben Aucamp, ACMREU001
import numpy as np
import pylab as plt
h=6.626*10**-34
c=3*10**8
T=[3000,4000,5000,6000]
v=np.linspace(0.1*10**-6,3*10**-6,100)
k=1.38*10**-23
#T=3000
B1=2*h*c**2*v**-5*(np.e**(h*c*(v*k*T[0])**-1)-1)**-1
max1=0.0029/T[0]
B11=2*h*c**2*max1**-5*(np.e**(h*c*(max1*k*T[0])**-1)-1)**-1
plt.plot(v,B1,'c')
plt.plot([max1,max1],[0,B11],'k')
#T=4000
B2=2*h*c**2*v**-5*(np.e**(h*c*(v*k*T[1])**-1)-1)**-1
max2=0.0029/T[1]
B22=2*h*c**2*max2**-5*(np.e**(h*c*(max2*k*T[1])**-1)-1)**-1
plt.plot(v,B2,'r')
plt.plot([max2,max2],[0,B22],'k')
#T=5000
B3=2*h*c**2*v**-5*(np.e**(h*c*(v*k*T[2])**-1)-1)**-1
max3=0.0029/T[2]
B33=2*h*c**2*max3**-5*(np.e**(h*c*(max3*k*T[2])**-1)-1)**-1
plt.plot(v,B3,'g')
plt.plot([max3,max3],[0,B33],'k')
#T=6000
B4=2*h*c**2*v**-5*(np.e**(h*c*(v*k*T[3])**-1)-1)**-1
max4=0.0029/T[3]
B44=2*h*c**2*max4**-5*(np.e**(h*c*(max4*k*T[3])**-1)-1)**-1
plt.plot(v,B4,'b')
plt.plot([max4,max4],[0,B44],'k')
#plt.xticks(v*10**6)

plt.show()

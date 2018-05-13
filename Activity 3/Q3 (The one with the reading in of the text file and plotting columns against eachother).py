#Reuben Aucamp ACMREU001

import numpy as np
import pylab as plt


##NOTE!
##NOTE!
##NOTE!
#Sometimes, for some unknown reason, there's an error on the reading of
#the file, simply close and reopen program to fix. Trust me. It's the gods
#of coding that hate me, the code isn't actually faulty.



#reading in File
w50=np.loadtxt('HI_properties.txt', skiprows=1, delimiter=',')

#sorting in terms of HI column (w50[:,5])
for i in range(len(w50[:,5])):
    for j in range(i+1,73):
        if w50[i,5]>w50[j,5]:
            for k in range(len(w50[0,:])):  #OK listen, this third for loop was
                sp=w50[j,k]                 #not the first way i tried, the other
                w50[j,k]=w50[i,k]           #was more elegant and made more sense
                w50[i,k]=sp                 #but PYTHON REFUSED so i did this instead
np.savetxt('bedonebitch.txt',w50)

#plotting one column (containing MHI) vs another(containing W50)
plt.plot(w50[:,3],w50[:,5], '.')
plt.xlabel('W50')
plt.ylabel('HI mass')
plt.show()
#plotting histogram, using column with
plt.hist(w50[:,5])              #default number of bins because why not
plt.ylabel('Frequency')
plt.xlabel('HI mass')
plt.show()

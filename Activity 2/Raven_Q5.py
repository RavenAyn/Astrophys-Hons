"Reuben Aucamp; ACMREU001"

import numpy as np

x=raw_input('Gimme a sentance to reverse: ')
c=np.chararray(len(x))
for i in range(0,len(x)):
    c[i]=x[len(x)-1-i]
print(c)

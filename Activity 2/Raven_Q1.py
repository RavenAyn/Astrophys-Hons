"Reuben Aucamp; ACMREU001"

import numpy as np

print('Enter Numbers to average below, enter -999 to submit numbers for averaging')
c=0
i=0
m=0
while i>=0:
    x=float(input('Number '+str(i+1)+ ': '))
    if x!=-999:
        c+=x
        i+=1
    else:
        m=(c/i)
        break
p=str(m)
print('Your Average is ' +p+ ' Isnt it beautiful')

import numpy as np
import random as r
import pylab as plt
c=0
n=0
m=0
q=10000.
j=int(q)
#when you wonder what kind of distribution the games will take
#g=np.zeros(j)

for i in range(j):
    c=0
    n=0
    while c<100:
        #Two die as opposed one random function cause the probability of a 2
        #bieng thrown is much less than the probability of a 6
        
        d1=r.randint(1,6)
        d2=r.randint(1,6)
        c+=d1+d2
        n+=1
        #ATTACK OF THE SNAKES AND REVENGE OF THE LADDERS
        if c==3:
            c=21
        elif c==8:
            c=30
        elif c==17:
            c=13
        elif c==28:
            c=84
        elif c==52:
            c=29
        elif c==57:
            c=40
        elif c==58:
            c=77
        elif c==62:
            c=22
        elif c==75:
            c=86
        elif c==80:
            c=100
        elif c==90:
            c=91
        elif c==95:
            c=51
        elif c==97:
            c=79
    m+=n
 #   g[i]=n
print ('average number of die throws required to finish the game ', + m/q)

#turns out its either poissonian or binomial but im lazy
#plt.hist(g, bins = 100)
#plt.show()
        

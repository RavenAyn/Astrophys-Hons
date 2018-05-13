import math
x=int(input("The Power!(your value of x): "))
n=int(input("The Order!(your value of n): "))
#x=2
#n=4
e=2.71828**x
p=1
for i in range(1,n):
    t=x**i/math.factorial(i)
    p=p+t
print(p)

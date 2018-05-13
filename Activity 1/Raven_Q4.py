
print("Lets find some root-y roots. Below choose a value for a, b and c of a polynomial and we will magic its roots into existance")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

#a=3
#b=6
#c=2

h=(-b+(b**2-4*a*c)**0.5)/(2*a)
j=(-b-(b**2-4*a*c)**0.5)/(2*a)

print('The higher intercept is:', h)
print('The lower intercept is: ', j)

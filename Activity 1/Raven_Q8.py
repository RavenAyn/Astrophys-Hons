print('Enter ye three numbers ye brave soul')

x=int(input('x= '))
y=int(input('y= '))
z=int(input('z= '))
h1=(x**2+y**2)**0.5
h2=(x**2+z**2)**0.5
h3=(y**2+z**2)**0.5
if x==h3:
    print('Tis a right-angled triangle with x as the Hypotenuse...ye live another day')
elif y==h2:
    print('Tis a right-angled triangle with y as the Hypotenuse...ye live another day')
elif z==h1:
    print('Tis a right-angled triangle with z as the Hypotenuse...ye live another day')
else:
    print('Tis not a right-angled triangle...and now youre dead')

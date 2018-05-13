
aleph='abcdefghijklmnopqrstuvwxyz'
#x='sohy'
x=input('your word please: ')
#b=aleph[(x.index('y'))]
#print(b)
c=aleph.index(x[-1])
#print(c)
if c==24:
    print(x[0:-1],'ies')
elif c==14:
    print(x[0:-2],'es')
elif c==7:
    print(x[0:-2],'es')
elif c==23:
    print(x[0:-2],'es')
elif c==25:
    print(x[0:-2],'es')
elif c==18:
    print(x[0:-2],'es')
else: 
    print(x,'s')

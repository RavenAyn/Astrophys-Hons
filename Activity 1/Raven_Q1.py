a=85
c=input('Guess a number between 0 and 99: ')
b=int(c)
i=1
if (b<a):
    print('sorry, thats too low')

elif (b>a):
    print('oops, youre too high')

elif (b==a):
    print('Well done! You got it!')

else:
    print('THOSE ARENT THE RULES, SO YOU DONT GET TO PLAY')


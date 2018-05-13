"Reuben Aucamp; ACMREU001"


a=32
print('You get 20 chances to guess a number between 0 and 99, if you get it, the world doesnt end,')
print('but if you dont, *boom*')
      
for i in range(20):
    if i==0:
        c=raw_input('Guess a number between 0 and 99: ')
        b=int(c)
        if (b<a):
            print('Sorry, thats too low')

        elif (b>a):
            print('Oops, youre too high')

        elif (b==a):
            print('Well done! You got it! Your world lives another sad day!')
            break

        else:
            print('THOSE ARENT THE RULES, SO YOU DONT GET TO PLAY')
    if i!=0:
        
        c=raw_input('Oh dear, try again, its only try number '+str(i+1)+': ')
        b=int(c)
        if (b<a):
            print('sorry, thats too low')

        elif (b>a):
            print('oops, youre too high')

        elif (b==a):
            print('Well done! You got it! Your world lives another sad day!')
            break

        else:
            print('THOSE ARENT THE RULES, SO YOU DONT GET TO PLAY')

        
    
if i==19:
    print('Lol please try harder next time. BOOM everyone you ever knew is dead now. Does it feel good. DOES IT')

Exercises - 2
1. Write some code that will prompt the user to enter as many numbers as they want
to. To indicate that they're done entering their numbers, they must enter the number
-999. Your code must then compute the mean of the numbers they entered (excluding
-999, obviously).
HINT 1: Before you start collecting the user's numbers, create a variable called
\number sum" that is initialised to 0. Then, each time the user enters a new number,
add that number to number sum. In other words, number sum is a running total of
the numbers that are being entered.
HINT 2: Create another variable before your loop called \N". Each time the user
enters a new numbers, increment its value by 1 (i.e. N=N+1). Then, once you're done
collecting numbers, the mean is simply number sum/N.
HINT 3: Use a break statement to exit the for loop when the user enters -999.
2. Use your \guess the number" code from the previous prac, and loop it. Use a loop to
execute the code 20 times. Once the user has guessed the correct number, break out
of the loop to end the game. If they don't guess the number within 20 attempts, tell
them they really should try harder next time.
3. Write some code that will prompt the user to enter a number, and then print to screen
the factorial of that number.
HINT: Supposed I have the loop for i in range(1,8):. Then, i takes on the
values 1, 2, 3, 4, 5, 6, 7 ... which can easily be combined to calculate 7!.
4. \99 Bottles of Beer" is a traditional song in the United States and Canada. It is pop-
ular to sing on long trips, as it has a very repetitive format which is easy to memorise,
and can take a long time to sing. The song's simple lyrics are as follows:
99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98
bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle. The song is com-
pleted when the singer or singers reach zero.
Write a Python program capable of generating all the verses of the song.
5. We've already learnt how to extract a single character from a string. Given two
characters, they can be \added" together to form a new string:
Page 1
In [2]: q='a'
In [3]: r='b'
In [4]: s=q+r
In [5]: print(s)
ab
In [6]: s
Out[6]: 'ab'
Write some code that will prompt the user to enter a string, and then use a for loop
to print the reversal of the string to the screen. For example, if the user enters \Here
I am", your code should output \ma I ereH".
HINT: At the start of your code create a string variable that will eventually con-
tain the reversal of the user's string. Initialise it to be equal to the last character of
the string entered by the user. Then, start \adding" the other characters to it.

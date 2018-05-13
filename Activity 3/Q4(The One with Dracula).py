import numpy as np

text_file = open("dracula.txt", "r")
lines = text_file.readlines()
vowel=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in range(63):
    for j in range(len(lines[i])):
        if lines[i][j] in vowel:
            c+=1
print (c)


#print (lines[0][0])
#print (len(lines[0])
text_file.close()

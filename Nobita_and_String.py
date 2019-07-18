#Doraemon gave Nobita a gadget that swaps words inside a string in the following manner :

#If there are W words, word 1 is swapped with word W, word 2 is swapped with word W-1 and so on. The problem is that Nobita himself cannot verify the answer for large strings. Help him write a program to do so.

#INPUT : 
#the first line of the input contains the number of test cases. Each test case consists of a single line containing the string.

#OUTPUT :
#output the string with the words swapped as stated above.

t = int(input())
x = []
for i in range(t):
    c = input()
    c = c.split(' ')
    c.reverse()
    x.append(c)
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=' ')
    print()

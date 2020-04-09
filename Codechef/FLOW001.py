'''
Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.

Program is very simple, Given two integers A and B, write a program to add these two numbers.
'''



t=int(input())
x=[]
sum=0
for i in range(t):
    s=input()
    x.append(s.split(' '))

for i in range(t):
    for j in range(len(x[i])):
        sum+=int(x[i][j])
    print(sum)
    sum=0

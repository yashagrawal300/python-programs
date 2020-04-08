'''Kostya likes the number 4 much. Of course! This number has such a lot of properties, like:'''


t=int(input())'''
x=[]
for i in range(t):
    s=input()
    x.append(s)
c=0
for i in range(t):
    for j in range(len(x[i])):
        if x[i][j]=='4':
            c+=1
        else:
            continue
    print(c)
    c=0

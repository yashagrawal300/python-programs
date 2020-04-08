'''If an Integer N, write a program to reverse the given number.'''


t=int(input())
x=[]
p=[]
for i in range(t):
    s=input()
    x.append(s)

for i in range(t):
    for j in range(0,-len(x[i]),-1):
        p.append(x[i][j-1])
    r=''.join(p)
    print(int(r))
    del p[0:len(p)]

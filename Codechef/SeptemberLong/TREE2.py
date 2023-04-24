# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    x = ( list(map(int,input().strip().split())))
    x = set(x)
    if 0 in x :
        print(len(x)-1)
    else :
        print(len(x))
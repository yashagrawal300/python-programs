t = int(input())
for i in range(t):
    s = list(input())
    x = list(input())
    s.sort()
    x.sort()
    s = ''.join(s)
    x = ''.join(x)
    for j in range(len(s)):
        if s[j] in x:
            if j == len(s)-1:
                print(x)
        else:
            print("Impossible")

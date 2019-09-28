t = int(input())
for i in range(t):
    s = list(input())
    x = list(input())
    x.sort()
    s = ''.join(s)
    for j in range(len(s)):
        if s[j] in x:
            x.remove(s[j])
            if j == len(s)-1:
                print(s, end= '')
                print(''.join(x))
        else:
            print("Impossible")
            break

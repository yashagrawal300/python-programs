'''You are provided an integer . Your task is to determine the largest integer  () that is a coprime of . This implies that .'''

y = int(input())
def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

s=[]
for i in range(y-1):
    if gcd(i, y)==1:
        s.append(i)
    else:
        continue
print(s[len(s)-1])

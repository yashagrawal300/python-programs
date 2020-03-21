'''The pattern challenge is back again with more complexity. Can you solve it??


3

2224 5262 223
'''

t = int(input())
s = list(map(int, input().split()))
s.sort()

print(s[0]+s[len(s)-1])

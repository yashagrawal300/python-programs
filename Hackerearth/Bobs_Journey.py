'''
Bob is travelling from one city to another. In his way, he sees many other cities pass by. What he does instead of learning the full names of the cities, he learns just the first character of the cities. For example, if he passes by "bhopal", he will just remember the 'b'.

Given the list of N cities that come in his way, print "YES" or "NO" depending on if he is able to remember all the cities distinctly or not.

Note: City name consists of small English alphabets only.
'''


t = int(input())

for i in range(t):
    d = int(input())
    q = []
    flag = 0
    for j in range(d):
        s = input()
        if s[0] in q:
            flag = 1
        else:
            q.append(s[0])
    if flag==0:
        print('YES')
    else:
        print("NO")

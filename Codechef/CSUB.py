'''
Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.

'''


t = int(input())

for i in range(t):
    y = int(input())
    x = list(map(int, input()))
    x.sort(reverse=True)
    count = 0

    for j in range(len(x)):
        if x[j] == 1:
            count += j + 1
        else:
            break

    print(count)

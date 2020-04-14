'''
Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input:
First line contains 2 space separated integers, N - total rows, M - total columns.
Each of the next N lines will contain M space separated integers.

Output:
Print M lines each containing N space separated integers.
'''





t = list(map(int, input().split()))

d = []

for i in range(t[0]):
    d.append(list(map(int, input().split())))



for i in range(t[1]):
    for j in range(t[0]):
        print(d[j][i], end = " ")
    print()
    

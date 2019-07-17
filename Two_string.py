#Given two strings of equal length, you have to tell whether they both strings are identical.

#Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

#Input :

#First line, contains an intger 'T' denoting no. of test cases.
#Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
#Output:

#For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.Given two strings of equal length, you have to tell whether they both strings are identical.

#Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

#Input :

#First line, contains an intger 'T' denoting no. of test cases.
#Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
#Output:

#For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.


t = int(input())
s=[]
for i in range(t):
    c = input()
    c = c.split(' ')
    for j in range(len(c)):
        c[j] = list(c[j])
        c[j].sort()
    if c[0]==c[1]:
        s.append('YES')
    else:
        s.append('NO')
for i in range(len(s)):
    print(s[i])

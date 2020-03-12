'''Problem Description

Given a series of integer pairs  and , output the sum of  and .

Input Format

Each line contains two integers,  and . One input file may contain several pairs  where .

Output Format

Output a single integer per line - The sum of  and .'''


# Write your code here
for i in range(7):
    t = list(map(int, input().split()))
    print(t[1]+t[0])

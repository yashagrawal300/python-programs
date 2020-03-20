'''You are given an array  of size  that contains integers. Here,  is an even number. You are required to perform the following operations:

Divide the array of numbers in two equal halves
Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
Generate a number by using the digits that have been selected in the above steps'''

t = int(input())
A = input()
A = A.split(' ')

y = []
for i in range(len(A)//2):
    y.append(A[i][0])
for i in range(len(A)//2, len(A), 1):
    y.append(A[i][len(A[i])-1])


y = ''.join(y)

if int(y)%11==0:
    print("OUI")
else:
    print("NON")


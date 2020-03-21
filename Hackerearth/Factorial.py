#You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

#Input Format:
#The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

#Output Format
#Output a single line denoting the factorial of the number N.

n = int(input())
answer=1
for i in range(1,n+1,1):
    answer*=i
print(answer)
    

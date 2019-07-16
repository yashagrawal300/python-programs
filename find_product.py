#You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo .

#Input Format:
#The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

#Output Format:
#Print a single integer denoting the product of all the elements of the array Modulo .


x = int(input())
c=input()
c = c.split(' ')
answer=1
for i in range(len(c)):
    answer=(answer* int(c[i]))%((10**9)+7)
print(answer)
    

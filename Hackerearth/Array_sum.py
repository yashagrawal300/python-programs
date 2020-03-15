#You are given an array of integers of size . You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

#Input Format

#The first line of the input consists of an integer . The next line contains space-separated integers contained in the array.

#Output Format

#Print a single value equal to the sum of the elements in the array.

t = int(input())
c = input()
c = c.split(' ')
count=0
for i in range(t):
    count+=int(c[i])
print(count)

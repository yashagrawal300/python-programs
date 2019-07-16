#You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

#Input Format
#The first and only line of input contains 3 space separated integers l, r and k.

#Output Format
#Print the required answer on a single line.

c=input()
c = c.split(' ')
count=0
for i in range(int(c[0]),int(c[1])+1,1):
    if i%int(c[2])==0:
        count+=1
    else:
        continue
print(count)

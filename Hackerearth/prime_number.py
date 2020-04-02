#You are given an integer N. You need to print the series of all prime numbers till N.

#Input Format

#The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

#Output Format

#Print the desired output in single line separated by spaces.





x=int(input())
s=[2]
y=0
for j in range(1,x+1,1):
    y=j
    for i in range(2,y+1//2,1):
        if y%i==0:
            break
        else:
            if y-1==i:
                s.append(y)
            else:
                continue
for i in range(len(s)):
    print(s[i], end=' ')

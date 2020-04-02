#You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

#Input Format
#The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

#Output Format
#Print the required answer on a single line.


x = input()
for i in range(0,len(x),1):
    if x[i]==x[len(x)-1-i]:
        if i==len(x)-1:
            print('YES')
        else:
            continue
    else:
        print('NO')
        break

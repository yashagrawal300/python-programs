#Mr. X's birthday is in next month. This time he is planning to invite N of his friends. He wants to distribute some chocolates to all of his friends after party. He went to a shop to buy a packet of chocolates.
#At chocolate shop, each packet is having different number of chocolates. He wants to buy such a packet which contains number of chocolates, which can be distributed equally among all of his friends.
#Help Mr. X to buy such a packet.

#Input:
#First line contains T, number of test cases.
#Each test case contains two integers, N and M. where is N is number of friends and M is number number of chocolates in a packet.

#Output:
#In each test case output "Yes" if he can buy that packet and "No" if he can't buy that packet.

t = int(input())
s=[]
for i in range(t):
    c = input()
    c = c.split(' ')
    if int(c[0])<int(c[1]):
        if int(c[1])%int(c[0]) == 0:
            s.append('Yes')
        else:
            s.append('No')
    else:
        s.append('No')
for i in range(len(s)):
    print(s[i])

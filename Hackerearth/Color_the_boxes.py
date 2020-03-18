'''You are given  boxes that are kept in a straight line. You are also given  colors such that (). You cannot change the position of boxes. Determine the number of ways to color the boxes such that if you select any  consecutive boxes then the color of each box is unique.

Since the number could be large, print the answer modulo .'''

x = input()
x = x.split(' ')
sum = 1
for i in range(1, int(x[1])+1, 1):
    sum = sum%(10**9+7)*(i)
print(sum%(10**9+7))

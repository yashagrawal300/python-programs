'''An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point  of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward.
Determine, what is the minimum number of steps he need to make in order to get to his friend's house.'''

t = int(input())
count = 0
count = t//5
if t%5==0:
    print(count)
else:
    print(count+1)

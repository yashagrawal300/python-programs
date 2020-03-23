'''
Jack is your friend and Sophia is his girlfriend. But due to some unknown reason ( unknown for us, they know it) Sophia started hating to Jack. Now, Jack is in big trouble but he has a solution, He knows that if he will gift T patterns of a particular type ( For pattern observation see the sample test cases) then Sophia will start loving again to Jack. But Jack is depressed now and need your help to gift her that type patterns of '*' and '#' of N lines. So, it's your responsibility to save your friend's relationship.
'''

t = int(input())
for i in range(t):
    x = int(input())
    for j in range(1, x+1, 1):
        for k in range(1, x*2+1, 1):
            if k<=j or (x*2+1)-j<=k:
                print("*", end = '')
            else:
                print("#", end = '')
        print()

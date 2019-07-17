#Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.


t = list(input())
ud = 0
lr = 0
for i in range(len(t)):
    if t[i]=='L':
        lr-=1
    elif t[i]=='R':
        lr+=1
    elif t[i]=='U':
        ud+=1
    elif t[i]=='D':
        ud-=1
    else:
        continue
print(lr, ud)

'''Two sisters, A and B, play the piano every day. During the day, they can play in any order. That is, A might play first and then B, or it could be B first and then A. But each one of them plays the piano exactly once per day. They maintain a common log, in which they write their name whenever they play.

You are given the entries of the log, but you're not sure if it has been tampered with or not. Your task is to figure out whether these entries could be valid or not.'''




t=int(input())
x=[]
for i in range(t):
    s=input()
    x.append(s)

for i in range(t):
    for j in range(0,len(x[i]),2):
        if x[i][j]==x[i][j+1]:
            print("no")
            break
        elif j==len(x[i])-2:
            print("yes")

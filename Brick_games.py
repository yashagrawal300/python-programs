#Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

#They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

#There are only N bricks, you need to help find the challenge result to find who put the last brick.

#Input:

#First line contains an integer N.

#Output:

#Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.


t = int(input())
count=0

for i in range(0,t,1):
    if count<=t:
        count+=i
        if count<=t:
            count+=i*2
        else:
            print('Patlu')
            break
    else:
        print('Motu')
        break


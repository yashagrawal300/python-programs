#Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like 

#So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows : 

#Window Seat : WS
#Middle Seat : MS
#Aisle Seat : AS

#You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

#INPUT
#First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

#OUTPUT
#For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.




x = [1, 3, 5, 7, 9, 11]
t = int(input())
s = []
d = ['WS', 'MS', 'AS', 'AS', 'MS', 'WS']
for i in range(t):
    c = int(input())
    f = c % 12
    if f <= 6:
        if f == 0:
            s.append(c - x[5])
            s.append(d[5])
        else:
            s.append(c + x[6 - f])
            s.append(d[6 - f])
    else:
        f = f - 6
        s.append(c - x[f - 1])
        s.append(d[f - 1])
for i in range(0, len(s), 2):
    print(s[i], s[i + 1])

#You are conducting a contest at your college. This contest consists of two problems and  participants. You know the problem that a candidate will solve during the contest.

#You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

#Use green-colored balloons for the first problem and purple-colored balloons for the second problem
#Use purple-colored balloons for the first problem and green-colored balloons for the second problem
#You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

#Input format

#First line:  that denotes the number of test cases ()
#For each test case: 
#First line: Cost of green and purple-colored balloons 
#Second line:  that denotes the number of participants ()
#Next  lines: Contain the status of users. For example, if the value of the  integer in the  row is , then it depicts that the participant has not solved the  problem. Similarly, if the value of the  integer in the  row is , then it depicts that the participant has solved the  problem.


t = int(input())
s = []
for i in range(t):
    cost = input()
    cost = cost.split(' ')
    for j in range(len(cost)):
        cost[j] = int(cost[j])
    cost.sort()
    r = 0
    l = 0
    n = int(input())
    for j in range(n):
        y = list(input())
        r += int(y[0])
        l += int(y[2])
    if r > l:
        r = r * int(cost[0])
        l = l * int(cost[1])
    else:
        r = r * int(cost[1])
        l = l * int(cost[0])
    a = l + r
    s.append(a)
for i in range(len(s)):
    print(s[i])

# Migaratory Birds (Link: https://www.hackerrank.com/challenges/migratory-birds/problem)

n = int(input())
take = input().split(" ")
length = int(max(take))
counter = 0
count = []
for i in range(1, length+1):
    for j in range(n):
        if(i == int(take[j])):
            counter += 1
    count.append(counter)
    counter = 0
print(count.index(max(count))+1)

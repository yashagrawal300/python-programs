'''A Little Elephant and his friends from the Zoo of Lviv like candies very much.

There are N elephants in the Zoo. The elephant with number K (1 ≤ K ≤ N) will be happy if he receives at least AK candies. There are C candies in all in the Zoo.

The Zoo staff is interested in knowing whether it is possible to make all the N elephants happy by giving each elephant at least as many candies as he wants, that is, the Kth elephant should receive at least AK candies. Each candy can be given to only one elephant. Print Yes if it is possible and No otherwise.
'''

# cook your dish here
t = int(input())

for i in range(t):
    d = list(map(int, input().split()))
    g = list(map(int, input().split()))
    if sum(g) <= d[1]:
        print("Yes")
    else:
        print("No")

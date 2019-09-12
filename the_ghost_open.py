'''PandeyG, a brilliant tennis player, decided to start a tournament in his colony. Now, since PandeyG is overly optimistic and ambitious - he tries to lure in as many people as he can from his colony for them to participate in his very own knockout type tennis tournament. What he fails to realize that, to have a knockout tournament, you need to have number of players, in the form of 2^a, where a is any number - what it simply means is that, if there are only 7 people to take part in the tournament, a knockout version cannot be held.

Because: 1 vs. 2 | 3 vs. 4 | 5 vs. 6 | 7 vs. ? |'''

t = int(input())

for i in range(t):
    x = int(input())
    if x==0:
        print(0)
    else:
        print(x-1)

'''
On the ice planet Hoth, Chef has run into his arch-nemesis, DarthForces. Darth has a peculiar fighting style ― he does not attack, but simply defends and lets his opponent tire himself out.

Chef has a lightsaber which has an attack power denoted by P. He keeps hitting Darth with the lightsaber. Every time he hits, Darth's health decreases by the current attack power of the lightsaber (by P points), and afterwards, P decreases to ⌊P2⌋.

If the attack power becomes 0 before Darth's health becomes 0 or less, Chef dies. Otherwise, Darth dies. You are given Darth's initial health H and the initial attack power P. Tell Chef if he can beat Darth or if he should escape.
'''



t = int(input())

for _ in range(t):
    h, p = map(int, input().split())
    flag = 0


    while p!=0:
        h-=p

        if h<= 0:
            print(1)
            flag = 1
            break

        p = p//2

    if flag ==0:
        print(flag)

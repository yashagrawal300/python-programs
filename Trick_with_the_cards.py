'''
Mr. X is performing a trick with the cards. He has N cards, lets name them 1.....N, on a round table. So card 1 is in between 2nd card and Nth card. Initially all cards are upside down. His trick involves making all cards face up.

His trick is whenever he taps on a card, it flips (if card was originally upside down, after flipping its faces up, and vice-versa), but he is no ordinary magician, he makes the two adjacent cards (if any) also to flip with the single tap. Formally, if he taps ith card, then i-1, i, i+1 cards are flipped. (Note that if he taps Nth card, then he flips (N-1)th, Nth and 1st card.)

Our magician needs a helper, to assist him in his magic tricks. He is looking for someone who can predict minimum number of taps needed to turn all the cards facing up.'''

t=int(input())
for i in range(t):
    x=int(input())
    if(x==2 or x==3):
        print("1")
    elif(x%3==0):
        print(x//3)
    else:
        print(x)

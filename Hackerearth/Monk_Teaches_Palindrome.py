'''
Monk introduces the concept of palindrome saying,"A palindrome is a sequence of characters which reads the same backward or forward."
Now, since he loves things to be binary, he asks you to find whether the given string is palindrome or not. If a given string is palindrome, you need to state that it is even palindrome (palindrome with even length) or odd palindrome (palindrome with odd length).
'''


t = int(input())

for i in range(t):
    f = list(input())

    if f[::-1]==f:
        if len(f)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")

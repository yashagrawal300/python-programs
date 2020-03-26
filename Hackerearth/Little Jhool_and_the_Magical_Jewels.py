'''Little Jhool is still out of his mind - exploring all his happy childhood memories. And one of his favorite memory is when he found a magical ghost, who promised to fulfill one of Little Jhool's wish.

Now, Little Jhool was a kid back then, and so he failed to understand what all could he have asked for from the ghost. So, he ends up asking him something very simple. (He had the intuition that he'd grow up to be a great Mathematician, and a Ruby programmer, alas!) He asked the ghost the power to join a set of *the letters r, u, b and y * into a real ruby. And the ghost, though surprised, granted Little Jhool his wish...

Though he regrets asking for such a lame wish now, but he can still generate a lot of real jewels when he's given a string. You just need to tell him, given a string, how many rubies can he generate from it?

Input Format:
The first line contains a number t - denoting the number of test cases.
The next line contains a string.

Output Format:
Print the maximum number of ruby(ies) he can generate from the given string.'''

t = int(input())
for i in range(t):
    x = input()
    s = [0,0,0,0]
    for j in range(len(x)):
        if x[j]=='r':
            s[0]+=1
        elif x[j]=='u':
            s[1]+=1
        elif x[j]=='b':
            s[2]+=1
        elif  x[j]=='y':
            s[3]+=1
    s.sort()
    print(s[0])

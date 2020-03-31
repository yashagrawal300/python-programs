'''You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.'''



t = input()
z = 0
o = 0

for i in range(len(t)):
    if t[i]=="z":
        z+=1
    else:
        o+=1


if 2*z==o:
    print("Yes")
else:
    print("No")

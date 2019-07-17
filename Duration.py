#Rahul is a very busy persion he dont wan't to waste his time . He keeps account of duration of each and every work. Now he don't even get time to calculate duration of works, So your job is to count the durations for each work and give it to rahul.

 

#Input:

#First line will be given by N number of works
#Next N line will be given SH,SM,EH and EM  each separated by space(SH=starting hr, SM=starting min, EH=ending hr, EM=ending min)
#Output:

#N lines with duration HH MM(hours and minutes separated by space)


t = int(input())
s=[]
for i in range(t):
    c = input()
    c = c.split(' ')
    h = 0
    m = 0
    a = int(c[0])*60+int(c[1])
    b = int(c[2])*60+int(c[3])
    d = b-a
    s.append(d//60)
    s.append(d%60)

for i in range(0, len(s),2):
    print(s[i], s[i+1])

'''Given a 32-bit signed integer, reverse digits of an integer.'''



class Solution(object):
    def reverse(self, x):

        x = str(x)

        flag = 0

        if x[0]=="-":
            flag = 1
        d = []   
        for i in range(0,len(x)-flag, 1 ):
            d.append(x[len(x)-i-1])

        c = int("".join(d))

        if flag==0:
            if 2**31<c:
                return 0
            else:
                return c
        else:
            if (-1)*2**31>c*(-1):
                return 0
            else:
                return c*(-1)

'''
Sample Testcases Input:
691 41
947 779

Sample Testcases Output:
1300
336

'''



from math import fabs


d = list(map(int, input().split()))

print(int(fabs(d[0]-d[1])*2))

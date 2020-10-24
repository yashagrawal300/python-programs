'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    
    def climbStairs(self, n: int) -> int:

        if n==1:
            return 1

        count = [1 ,2 ]

        for i in range(2, n):
            count.append(count[i-1] + count[i-2])

        return count[-1]

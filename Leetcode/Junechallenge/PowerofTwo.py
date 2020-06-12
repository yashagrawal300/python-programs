'''
Given an integer, write a function to determine if it is a power of two.
'''



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n and (not(n & (n - 1))) ):
            return True
        else:
            return False
        

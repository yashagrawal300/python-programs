class Solution:
    def minOperations(self, n: int) -> int:
        
        ans = 0
        
        target = (1 + (2*(n-1) + 1))//2

        
        
        i = 1
        
        while i <= target:
            ans+= target - i
            i+=2
        
        return ans

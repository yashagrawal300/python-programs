'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

For example, given an input list of values [1, 9], when we pick up a number out of it, the chance is that 9 times out of 10 we should pick the number 9 as the answer.
'''



class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        
        prev = 0
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + prev
            prev = self.w[i]
        
        self.maximum = self.w[-1]
        

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.maximum)
        
        left = 0
        right = len(self.w)-1
        while left < right:
            mid = (left+right)//2
            
            if self.w[mid] >= random_num:
                right = mid
            else:
                left = mid+1
        return right
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

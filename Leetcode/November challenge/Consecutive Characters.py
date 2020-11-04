
'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

'''


class Solution:
    def maxPower(self, s: str) -> int:
        
        count = 1
        
        h = 1
        
        for i in range(len(s) -1) :
            if s[i] == s[i+1]:
                h+=1
            
            else:
                count = max(count, h)
                h = 1
        count = max(count, h)
        return count
                
                
        

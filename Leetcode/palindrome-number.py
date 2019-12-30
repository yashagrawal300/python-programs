'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        d = []
        for i in range(len(x)):
            d.append(x[len(x)-i-1])
        d = ''.join(d)
        if x==d:
            return True
        else:
            return False
            

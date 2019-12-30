'''Given an integer number n, return the difference between the product of its digits and the sum of its digits.'''


class Solution(object):
    def subtractProductAndSum(self, n):
        n = str(n)
        add = 0
        product = 1
        for i in range(len(n)):
            add += int(n[i])
            product*= int(n[i]) 
        return product-add
 
 
 
 

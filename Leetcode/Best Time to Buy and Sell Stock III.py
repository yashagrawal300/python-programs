#Best Tiem to Buy and Sell -III
#Leetcode August

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        
        max = 0
        curr = prices[-1]
        
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>=curr:
                curr = prices[i]
                
            else:
                mn = prices[0]
                mx = 0
                
                for j in prices[0:i]:
                    if mn>j:
                        mn = j
                    elif j-mn>mx:
                        mx = j-mn
                        
                profit = curr-prices[i] + mx
                if max<profit:
                    max = profit

        return max
        

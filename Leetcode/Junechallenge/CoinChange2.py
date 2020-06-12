'''You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 '''
 
 
 
 class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        w = [0 for i in range(amount + 1)]
        w[0] = 1 
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    w[i] = w[i] + w[i - coin]
        return w[-1] 

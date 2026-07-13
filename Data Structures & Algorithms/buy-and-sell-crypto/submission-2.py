class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        profit = 0
        max_profit = 0
        for i, n in enumerate(prices):
            if n < lowest_price:
                lowest_price = n
            profit = prices[i] - lowest_price
            if max_profit < profit:
                max_profit = profit
                
            
            
        return max_profit
            
        

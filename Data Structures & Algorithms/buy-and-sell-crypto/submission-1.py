class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        profit = 0
        max_profit = 0
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            profit = price - lowest_price
            if max_profit < profit:
                max_profit = profit
                
            
            
        return max_profit
            
        

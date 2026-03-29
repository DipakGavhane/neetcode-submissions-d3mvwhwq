class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]
            else:
                profit = prices[i] - buying_price
                max_profit = max(max_profit, profit)
                
        return max_profit
            
            

            


        
                
            


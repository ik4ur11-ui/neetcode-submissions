class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            right = prices[-(len(prices)- i):]
            profit = max(right) - prices[i]
            if profit > max_profit:
                max_profit = profit

        return max_profit
        
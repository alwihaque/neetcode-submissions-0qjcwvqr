class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - start
            max_profit = max(max_profit, profit)
            start = min(start, prices[i])
        return max_profit


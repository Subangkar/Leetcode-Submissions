class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_so_far = prices[0]
        max_diff = 0

        for i in range(len(prices)):
            diff = prices[i] - min_so_far
            if diff > max_diff:
                max_diff = diff                
            elif prices[i] < min_so_far:
                min_so_far = prices[i]

        return max_diff
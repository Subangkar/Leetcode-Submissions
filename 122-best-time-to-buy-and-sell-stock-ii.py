class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_so_far = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] <= max_so_far:
                # sell immediately and buy new if I find a price fall/same price
                profit += (max_so_far-min_so_far)
                min_so_far = prices[i]
                max_so_far = prices[i]
            elif prices[i] > max_so_far:
                # has the best price so far. So consider for selling
                max_so_far = prices[i]
        profit += (max_so_far-min_so_far) # if there was any sell on the last day
        return profit
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)

        dp[0] = 0
        for t in range(amount+1):
            for v in coins:
                if v<=t:
                    dp[t] = min(dp[t], 1 + dp[t-v])
        
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
        
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        inf = 0
        
        dp = [[inf]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                reward_match = 0
                if text1[i-1]==text2[j-1]:
                    reward_match = 1
                
                dp[i][j] = max(
                    reward_match + dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1],
                )

        return dp[-1][-1]        
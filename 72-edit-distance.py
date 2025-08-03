class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        inf = m+n+1
        
        dp = [[inf]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        dp[0][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                cost_sub = 1
                if word1[i-1]==word2[j-1]:
                    cost_sub = 0
                
                dp[i][j] = min(
                    cost_sub + dp[i-1][j-1],
                    1 + dp[i-1][j],
                    1 + dp[i][j-1],
                )


        # for i in range(m+1):
        #     for j in range(n+1):
        #         print(dp[i][j], end=' ')
        #     print()

        return dp[m][n]
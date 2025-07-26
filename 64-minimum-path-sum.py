class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = (200+200)*201
        dp = [[inf]*(n+1) for _ in range(m+1)]
        dp[1][0] = 0
        dp[0][1] = 0
        # dp[1][1] = grid[0][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1]) #, dp[i-1][j+1]
        # print(m, n)
        # for i in range(m+1):
        #     for j in range(n+1):
        #         print(dp[i][j], end=' ')
        #     print()                
        return dp[-1][-1]
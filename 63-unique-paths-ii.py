class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])
        default = 0
        dp = [[default]*(n) for _ in range(m)]
        for i in range(m):
            if grid[i][0]==1:
                break
            dp[i][0] = 1
        for j in range(n):
            if grid[0][j]==1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]!=1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(m, n)
        # for i in range(m):
        #     for j in range(n):
        #         print(dp[i][j], end=' ')
        #     print()                
        return dp[-1][-1]        
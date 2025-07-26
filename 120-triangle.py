class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        inf = 100000
        dp = [[inf]*(len(triangle)) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j]) #, dp[i-1][j+1]
        
        # for i in range(len(triangle)):
        #     for j in range(i+1):
        #         print(triangle[i][j], end=' ')
        #     print()
        # for i in range(len(triangle)):
        #     for j in range(len(triangle)):
        #         print(dp[i][j], end=' ')
        #     print()
        return min(dp[-1])

        
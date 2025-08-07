class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j]=="1" and not vis[i][j]:
                vis[i][j]=True
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        count = 0   
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not vis[i][j]:
                    count += 1
                    dfs(i, j)
        
        return count
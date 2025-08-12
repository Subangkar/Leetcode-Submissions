class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            # print(i+1, j+1)
            if 0<=i<m and 0<=j<n and board[i][j]=="O" and not vis[i][j]:
                vis[i][j]=True
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        for i in (0, m-1):
            for j in range(n):
                if board[i][j]=="O" and not vis[i][j]:
                    dfs(i, j)

        for j in (0, n-1):
            for i in range(1, m-1):
                if board[i][j]=="O" and not vis[i][j]:
                    dfs(i, j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j]=="O" and not vis[i][j]:
                    board[i][j] = "X"

        
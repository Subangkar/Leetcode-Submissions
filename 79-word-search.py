class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        T = len(word)
        vis = [[False]*n for _ in range(m)]

        def backtrack(i, j, t):
            # print(i,j,t,s)
            if t==T:
                return True
            if i<0 or j<0 or i==m or j==n or vis[i][j] or (t>0 and board[i][j] != word[t]):
                # if i>=0 and j>=0 and i<m and j<n:
                #     print(word[:t+1], i, j, t, s+board[i][j], word[t])
                return False
            if board[i][j] != word[t]:
                return False
            vis[i][j] = True
            res = backtrack(i, j+1, t+1) or backtrack(i+1, j, t+1) or backtrack(i, j-1, t+1) or backtrack(i-1, j, t+1)
            vis[i][j] = False
            return res

        for i in range(m):
            for j in range(n):
                if(backtrack(i, j, 0)): 
                    return True
        return False
        
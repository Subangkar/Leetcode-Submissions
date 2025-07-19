class Solution:

    def count_alive(self, board, i, j):
        m,n = len(board), len(board[0])
        if i<0 or j<0 or i>=m or j>=n:
            return 0
        else:
            return int(self.was_alive(board[i][j]))
        

    def was_alive(self, x) -> bool:
        # dead: 0->0 or 0->-1(now alive)
        # alive: 1->1 or 1->2(now dead)
        return x>0

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        def f(x,y):
            return self.count_alive(board,x,y)
        for i in range(m):
            for j in range(n):
                alive_count = f(i-1, j-1)+f(i-1, j)+f(i-1, j+1)+f(i, j-1)+f(i, j+1)+f(i+1, j-1)+f(i+1, j)+f(i+1, j+1)
                if board[i][j]==1:
                    if alive_count<2 or alive_count>3:
                        board[i][j] = 2
                else:
                    if alive_count==3:
                        board[i][j] = -1                  

        replace_map = {0:0, 1:1, -1:1, 2:0}
        for i in range(m):
            for j in range(n):
                board[i][j] = replace_map[board[i][j]]

        
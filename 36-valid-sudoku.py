class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sqr_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                sq_i = i//3
                sq_j = j//3
                if board[i][j] in row_sets[i] or board[i][j] in col_sets[j] or board[i][j] in sqr_sets[sq_i][sq_j]:
                    return False
                elif board[i][j]!='.':
                    row_sets[i].add(board[i][j])
                    col_sets[j].add(board[i][j])
                    sqr_sets[sq_i][sq_j].add(board[i][j])
        return True

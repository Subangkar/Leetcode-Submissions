class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False        
        first_col_has_zero = False
        
        
        # check if the first row contains zero
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column contains zero
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, m):
            if matrix[r][0] == 0:
                matrix[r] = [0]*n

        for c in range(1, n):
            if matrix[0][c] == 0:
                for i in range(m):
                    matrix[i][c] = 0

        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0
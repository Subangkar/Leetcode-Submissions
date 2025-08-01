class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def i_to_r_c(i):
            row = i//n
            col = i - row*n
            return row, col

        def val(i):
            r, c = i_to_r_c(i)
            return matrix[r][c]

        def bsearch(left, right):
            if left>right:
                return False
            mid = (left + right)//2
            midval = val(mid)
            if target < midval:
                return bsearch(left, mid-1)
            elif target > midval:
                return bsearch(mid+1, right)
            return True
            
        return bsearch(0, m*n-1)            




        
        
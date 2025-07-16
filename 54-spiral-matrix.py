class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lc = 0
        rc = n-1
        tr = 0
        br = m-1
        
        flat = []
        i = 0
        j = 0
        dir_i = 0
        dir_j = 1
        dirt = 1 # R, D, L, U
        
        while True:
            flat.append(matrix[i][j])
            if len(flat)==m*n:
                break
            if dirt==1 and j==rc:
                # rc -= 1
                tr += 1
                dir_i = 1
                dir_j = 0
                dirt = 2
            elif dirt==2 and i==br:
                # br -= 1
                rc -= 1
                dir_i = 0
                dir_j = -1
                dirt = 3
            elif dirt==3 and j==lc:
                # br -= 1
                br -= 1
                dir_i = -1
                dir_j = 0
                dirt = 4
            elif dirt==4 and i==tr:
                # br -= 1
                lc += 1
                dir_i = 0
                dir_j = 1
                dirt = 1
            i += dir_i
            j += dir_j
        
        return flat


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_2d_mat = []
        current_index = numRows
        direction = -1
        str_idx = 0
        l = len(s)
        new_l = 0
        while str_idx < l:
            if current_index == 1:
                current_index = numRows
            if current_index == numRows:
                colm_str = s[str_idx:min(l, str_idx + numRows)]
                str_idx += numRows
            else:
                colm_str = ' ' * (current_index - 1) + s[str_idx] + ' ' * (numRows - current_index)
                str_idx += 1
            colm = [x for x in colm_str]
            new_l += len(colm)
            str_2d_mat.append(colm)
            current_index += direction

        s_modified = ""
        s_modified_len = 0
        # print(str_2d_mat, new_l)
        numColms = len(str_2d_mat)
        for c in range(numRows):
            for r in range(numColms):
                # if s_modified_len == new_l:
                #     return s_modified
                # print(str_2d_mat[r][c], end='')
                if (r != numColms - 1 or (r == numColms - 1 and c < len(str_2d_mat[numColms - 1]))) and str_2d_mat[r][
                    c] != ' ':
                    s_modified += str_2d_mat[r][c]
                    s_modified_len += 1
            # print()
            # s_modified += "\n"
        return s_modified

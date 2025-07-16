class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        # print(rows)
        dir = 1
        currow = 0
        for i in range(len(s)):
            rows[currow].append(s[i])
            if currow == (numRows-1):
                dir = -1
            elif currow == 0:
                dir = 1
            # print(currow)
            currow = (currow+dir)%numRows # to handle single row case
        flat_list = [char for sublist in rows for char in sublist]
        return ''.join(flat_list)
        
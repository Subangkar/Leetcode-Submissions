class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # def r_c_to_val(r, c):
        #     if r%2==0:
        #         return r*n + c + 1
        #     else:
        #         return r*n+ n - c + 1
        
        def val_to_r_c(val):
            r = (val-1)//n
            c = (val-1)%n
            if r%2!=0:
                c = n-1-c
            r = n-r-1
            return r, c

        vis = [False]*(n*n+1)
        # par = [-1]*(n*n+1)
        q = deque([(1, 0)])
        vis[1] = True
        # par[1] = -1
        while q:
            cur, l = q.popleft()
            if cur==n*n:
                # x = cur
                # for i in range(l):
                #     print(x, end=' ')
                #     x = par[x]
                return l
            # r, c = val_to_r_c(cur)
            # print(cur, '->:', f'[{r},{c}]', end=' ')
            for i in range(cur+1, min(cur + 6, n*n)+ 1):
                nbr = i
                r, c = val_to_r_c(nbr)
                if board[r][c]!=-1:
                    nbr = board[r][c]
                if not vis[nbr]:
                    # print('(', nbr, l+1, ')', end=' ')
                    q.append([nbr, l+1])
                    # par[nbr] = cur
                    vis[nbr] = True
            # print()
        return -1        
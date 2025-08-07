class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        parens = []
        curren = list("_"*(2*n))
        # print(curren)
        def dfs(oppar, clpar, i):
            if i==2*n:
                # print(''.join(curren))
                parens.append(''.join(curren))
                return
            # print(i)
            if oppar < n:
                curren[i] = "("
                dfs(oppar+1, clpar, i+1)
            if clpar < oppar:
                curren[i] = ")"
                dfs(oppar, clpar+1, i+1)
            
        dfs(0, 0, 0)
        return parens
        
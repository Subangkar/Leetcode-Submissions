class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        candidate = [0]*k
        def backtrack(take_from, pos):
            if pos==k:
                res.append(candidate.copy())
                return
            for x in range(take_from, n+1):
                # print(pos)
                candidate[pos] = x
                # print(candidate)               
                backtrack(x+1, pos+1)
            
        backtrack(1, 0)
        return res


        
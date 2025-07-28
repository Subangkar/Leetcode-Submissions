class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        candidate = nums
        n = len(nums)
        def backtrack(i):
            if i == n-1:
                # print(candidate)               
                res.append(candidate.copy())
                return
            for j in range(i, n):
                # print(pos)
                candidate[i], candidate[j] = candidate[j], candidate[i]
                # print(candidate)               
                # res.append(candidate.copy())
                backtrack(i+1)
                candidate[i], candidate[j] = candidate[j], candidate[i]
            
        backtrack(0)
        return res    
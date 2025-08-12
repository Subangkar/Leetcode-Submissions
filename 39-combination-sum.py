class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = [0 for _ in range(target+1)]

        def backtrack(i, candidate_i, running_sum):
            if running_sum==target:
                result.append(current[:i])
                return
        
            if running_sum>target or i==len(current):
                return

            for j in range(candidate_i, len(candidates)):
                current[i] = candidates[j]
                backtrack(i+1, j, running_sum + candidates[j])

        backtrack(0, 0, 0)
        return result
            


        
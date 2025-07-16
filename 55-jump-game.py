class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False]*len(nums)
        reachable[0] = True
        for i in range(len(nums)-1):
            if reachable[i] == False:
                continue
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                reachable[j] = True
        return reachable[len(nums)-1]
            
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        max_lis = 1
        for i in range(1, n):            
            for j in range(i-1, -1, -1):
                if nums[j]<nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
            max_lis = max(lis[i], max_lis)
        
        # print(lis)
        return max_lis

        
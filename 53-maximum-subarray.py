class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_max = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            running_max = max(nums[i], running_max + nums[i])          
            max_sum = max(running_max, max_sum)

        return max_sum
                    
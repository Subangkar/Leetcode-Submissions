class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        running_max = nums[0]
        running_min = nums[0]
        total_sum = nums[0]

        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            running_max = max(nums[i], running_max + nums[i])
            running_min = min(nums[i], running_min + nums[i])
            total_sum += nums[i]
            
            max_sum = max(running_max, max_sum)
            min_sum = min(running_min, min_sum)

        # print(max_so_far, total_sum-min_so_far)
        if min_sum == total_sum:
            return max_sum
        return max(max_sum, total_sum-min_sum)

        
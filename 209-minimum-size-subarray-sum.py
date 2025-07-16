class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        i=0
        j=0
        n = len(nums)
        running_sum = 0
        running_sum_len = 0
        min_sum_gt_target_len = len(nums)+1
        while i<n:
            # running_sum not including j
            # print(f'[{i}, {j}]//{j-i} - {running_sum} // {min_sum_gt_target_len}')
            if running_sum<target:
                # if sum not met, extend on right
                if j<n:
                    running_sum += nums[j]
                    j = j+1
                    continue
                else:
                    break
            else:
                # if sum is met, note this range and shrink on left
                running_sum_len = j-i
                if running_sum_len<min_sum_gt_target_len:
                    min_sum_gt_target_len = running_sum_len
                running_sum -= nums[i]
                i = i + 1
        if min_sum_gt_target_len == len(nums)+1:
            min_sum_gt_target_len = 0
        return min_sum_gt_target_len

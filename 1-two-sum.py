class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums, actual_idx = zip(*sorted(zip(nums, range(len(nums))), key=lambda x: x[0]))
        # nums.sort()
        i=0
        j=len(nums)-1

        while i<j:
            if nums[i]+nums[j]<target:
                i = i+1
            elif nums[i]+nums[j]>target:
                j = j-1
            else:
                return [actual_idx[i],actual_idx[j]]
        
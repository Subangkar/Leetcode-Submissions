class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(k+1, len(nums)):
            if nums[i]!=nums[k]:
                nums[k+1] = nums[i]
                k = k +1
        return k+1
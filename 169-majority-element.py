class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candt = -1

        for i in range(len(nums)):
            if count==0:
                candt = nums[i]
                count += 1
            elif candt == nums[i]:
                count += 1
            else:
                count -= 1
        
        return candt
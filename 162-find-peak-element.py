class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2 or nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        
        l = 1
        r = n-2
        while l<=r:
            m = (l+r)//2
            # print(l, r, nums[l:r+1])
            # no need to think corner case here as m!=0 or n-1, we handled those in first
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            if nums[m]<nums[m+1]:
                l = m+1
            else:
                r = m-1
        return m
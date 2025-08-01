class Solution:
    def findMin(self, nums: List[int]) -> int:

        val = nums[0]
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            # print(val, nums[l], nums[m], nums[r], nums[l: r+1])
            if nums[l]<=nums[m]: 
                # this half sorted, note min and look for breakpoint in other half
                val = min(nums[l], val)
                l = m + 1
            else:
                val = min(nums[m], val)
                r = m - 1
                # break
        return val        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        key_f = -1
        key_l = -1

        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            # print(nums[m], nums[l: r+1])
            if nums[m]<target:
                l = m + 1
            elif nums[m]>target:
                r = m - 1
            else:
                key_f = m
                r = m - 1

        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            # print(nums[m], nums[l: r+1])
            if nums[m]<target:
                l = m + 1
            elif nums[m]>target:
                r = m - 1
            else:
                key_l = m
                l = m + 1

        return (key_f, key_l)
        
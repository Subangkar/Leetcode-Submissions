class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            # print(nums[l], nums[m], nums[r], nums[l: r+1])
            if nums[m]==target:
                return m
            if (nums[l] <= target <= nums[m]) or (nums[m] < nums[l] <= target) or (target <= nums[m] < nums[l]):
                r = m - 1
            # elif (nums[m] <= target <= nums[r]) or (target <= nums[r] <= nums[m]):
            #     l = m + 1
            else:
                l = m + 1
                # break
        return -1
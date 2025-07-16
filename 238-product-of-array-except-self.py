class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = [1]*len(nums)
        rm = [1]*len(nums)

        for i in range(1, len(nums)):
            lm[i] = lm[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rm[i] = rm[i+1]*nums[i+1]        

        return [lm[i]*rm[i] for i in range(len(nums))]
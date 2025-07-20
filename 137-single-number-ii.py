class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count_1s = 0
            for v in nums:
                count_1s += int((v&(1<<i))>0)
            if count_1s%3!=0:
                ans |= (1<<i)
        if ans>0x7FFFFFFF:
            ans -= 2**32
        return ans
        
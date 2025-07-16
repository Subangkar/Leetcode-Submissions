class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums)==0:
            return ranges
        a = nums[0]
        i = 1
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]+1:
                b = nums[i-1]
                if a==b:
                    ranges.append(f"{a}")
                else:
                    ranges.append(f"{a}->{b}")
                a = nums[i]

        b = nums[-1]
        if a==b:
            ranges.append(f"{a}")
        else:
            ranges.append(f"{a}->{b}")
        return ranges

        
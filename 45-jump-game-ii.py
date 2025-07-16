class Solution:
    def jump(self, nums: List[int]) -> int:

        current_end = 0
        farest_end = 0
        jump_count = 0

        for i in range(len(nums)-1):
            farest_end = max(i + nums[i], farest_end)
            if i == current_end:
                jump_count += 1
                current_end = farest_end
        return jump_count
        
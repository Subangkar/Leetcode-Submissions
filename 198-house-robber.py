class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0]*(len(nums)+1), [0]*(len(nums)+1)]
        # 0 not taking current, 1 may take current
        dp[0][1]=0
        dp[1][1]=nums[0]

        for i in range(1, len(nums)):
            dp[0][i+1] = dp[1][i]
            dp[1][i+1] = max(dp[0][i] + nums[i], dp[1][i])
            # print('0:', dp[0])
            # print('1:', dp[1])
        
        return max(dp[0][len(nums)], dp[1][len(nums)])


        
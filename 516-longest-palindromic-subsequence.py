class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        # start = [[-1]*(len(s)+1) for _ in range(len(s)+1)]
        
        for i in range(1, len(s)+1):
            dp[i][i] = 1
            # start[i][i] = i
        for l in range(2, len(s)+1):
            for i in range(1, len(s)-l+1+1):
                j = i + l - 1
                if s[i-1]==s[j-1] and dp[i][j] < 2 + dp[i+1][j-1]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    # start[i][j] = i
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    # start[i][j] = start[i+1][j]
                # print(i,j, s[i-1], s[j-1], dp[i][j], [l_i])
                # print()
        # for i in range(len(s)+1):
        #     for j in range(len(s)+1):
        #         print(dp[i][j], end=' ')
        #     print()

        # print('>')
        # for i in range(len(s)+1):
        #     for j in range(len(s)+1):
        #         print(f'{start[i][j]}', end=' ')
        #     print()

        max_len = dp[1][len(s)]
        # l_i = start[1][len(s)] - 1
        return max_len
        
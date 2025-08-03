class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*(len(s)+1) for _ in range(len(s)+1)]
        
        max_len = 1
        max_start = 0
        for i in range(1, len(s)+1):
            dp[i][i] = True
        for l in range(2, len(s)+1):
            for i in range(1, len(s)-l+1+1):
                j = i + l - 1
                if s[i-1]==s[j-1]:
                    dp[i][j] = (l<3) or dp[i+1][j-1]
                    if dp[i][j] and l>max_len:
                        max_len = l
                        max_start = i-1
                # print(i,j, s[i-1], s[j-1], dp[i][j], [l_i])
                # print()
        # for i in range(len(s)+1):
        #     for j in range(len(s)+1):
        #         print(dp[i][j], end=' ')
        #     print()

        return s[max_start:max_start+max_len]

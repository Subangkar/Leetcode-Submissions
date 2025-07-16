class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        idx = {}

        left = 0
        right = 0
        max_len = 0

        while right<len(s):
            if s[right] in idx:
                last_idx_of_right = idx[s[right]]
                while left<=last_idx_of_right:
                    del idx[s[left]]
                    left += 1
                idx[s[right]] = right
            else:
                idx[s[right]] = right
                cur_len = right - left + 1
                if cur_len>max_len:
                    max_len = cur_len
            right = right + 1 # safe hence moving left border cannot increase length 
        return max_len
            
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs = [0]*26
        ft = [0]*26

        base_ascii = ord('a')

        for i in range(len(s)):
            fs[ord(s[i])-base_ascii] += 1

        for i in range(len(t)):
            ft[ord(t[i])-base_ascii] += 1

        return fs==ft
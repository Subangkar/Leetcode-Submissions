class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if(len(magazine)<len(ransomNote)):
            return False

        fr = [0]*26
        fm = [0]*26

        for i in range(len(ransomNote)):
            fr[ord(ransomNote[i])-ord('a')] += 1
        for i in range(len(magazine)):
            fm[ord(magazine[i])-ord('a')] += 1

        for i in range(26):
            if fm[i]<fr[i]:
                return False
        return True
        
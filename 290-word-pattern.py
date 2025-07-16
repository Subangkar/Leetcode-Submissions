class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        # inv_mp = {}
        words = s.split()
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mp and mp[pattern[i]]!=words[i]:
                return False
            if pattern[i] not in mp and words[i] in mp.values():
                return False
            mp[pattern[i]] = words[i]
        return True
            
            
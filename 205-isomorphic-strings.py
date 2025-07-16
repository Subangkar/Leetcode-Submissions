class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap = {}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in cmap:
                if cmap[s[i]] != t[i]:
                    return False
                else:
                    continue
            if t[i] in cmap.values():
                return False
            
            cmap[s[i]] = t[i]
            
        return True

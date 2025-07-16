class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            '(':')',
            '{':'}',
            '[':']',
        }
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            elif not stack or mp[stack.pop()]!=s[i]: 
                return False
        return stack==[]
        
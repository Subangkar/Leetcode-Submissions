class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        def to_lower(char):
            if 'A'<=char<='Z':
                return chr(ord(char) + 32)
            else:
                return char
        def is_alphanum(char):
            return 'A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9'

        while i<j:
            if not is_alphanum(s[i]):
                i+=1
                continue
            if not is_alphanum(s[j]):
                j-=1
                continue

            l = to_lower(s[i])
            r = to_lower(s[j])

            if l!=r:
                return False
            i+=1
            j-=1
            
        return True
        
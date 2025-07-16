class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000,
        }
        
        sum = 0
        for i in range(len(s)-1):
            dval = 0
            if value[s[i]] < value[s[i+1]]:
                dval = -value[s[i]]
            else:
                dval = value[s[i]]
            sum += dval
        sum += value[s[len(s)-1]]
        return sum
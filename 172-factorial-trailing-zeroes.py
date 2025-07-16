class Solution:
    def trailingZeroes(self, n: int) -> int:
        cn0 = 0
        fct = 5
        
        while n>=fct:
            cn0 += (n//fct)
            fct *= 5
            
        return cn0
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base, exponent):
            if exponent == 0:
                return 1.0
            half = fast_pow(base, exponent // 2)
            if exponent % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            result = fast_pow(1/x, -n)
        else:
            result = fast_pow(x, n)                    
        return result
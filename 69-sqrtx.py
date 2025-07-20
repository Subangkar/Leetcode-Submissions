class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = x

        while l<=r:
            v = (l+r)//2
            if v*v<x:
                l=v+1
                res=v
            elif v*v>x:
                r=v-1
            else:
                res=v
                break
        return res


        
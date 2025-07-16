class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDgSq(v):
            sum = 0
            while v!=0:
                dg = v%10
                sum += (dg*dg)
                v=v//10
            return sum
        
        st = set()
        nv = n
        while nv!=1:
            nv = sumDgSq(nv)
            if nv in st:
                if nv==1:
                    return True
                return False
            st.add(nv)
        return True
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            v = i
            c = 0
            while v!=0:
                if v&1!=0:
                    c += 1
                v >>= 1
            ans.append(c)
        return ans
        
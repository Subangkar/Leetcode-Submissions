class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ntoggled_bits = 0
        while left!=right:
            ntoggled_bits += 1
            left >>= 1
            right >>= 1
        return (left<<ntoggled_bits)

        
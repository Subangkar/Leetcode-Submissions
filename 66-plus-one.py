class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        c_n = 0
        c_o = 1
        while i>=0:
            c_n = (digits[i]+c_o)//10
            digits[i] = (digits[i]+c_o)%10
            c_o = c_n
            i -= 1
        if c_o!=0:
            digits = [c_o] + digits
        return digits
            
        
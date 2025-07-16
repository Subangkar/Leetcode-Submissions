import re
class Solution:
    def myAtoi(self, str: str) -> int:
        val=0
        try:
            val=int( re.match('[ ]*([\+\-]{0,1}[0-9]+).*', str).group(1))
            # val=int(str.strip().split('.A-z ')[0])
            # val=int(val)
            val=max(val, -2**31)
            val=min(val, 2**31-1)
        except:
            val=0
        return val
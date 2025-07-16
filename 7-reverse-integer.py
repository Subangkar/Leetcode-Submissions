class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_x = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        while x != 0:
            rev_x = rev_x * 10 + (x % 10)
            x = int(x / 10)

        if rev_x > 2147483647 or rev_x < -2147483648:
            return 0

        return rev_x * sign


# print(Solution().reverse(x=-2147483648))
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_x = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        while x != 0:
            rev_x = rev_x * 10 + (x % 10)
            x = int(x / 10)

        if rev_x > 2147483647 or rev_x < -2147483648:
            return 0

        return rev_x * sign


# print(Solution().reverse(x=-2147483648))

class Solution:
    def divide(self, dividend, divisor):
        count = 0
        res = 0
        if dividend > 2 ** 31:
            return 6184773855
        if dividend < -2 ** 31:
            return -6184773855

        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i *= 2
                temp *= 2
        if not positive:
            res = -res

        return min(max(-2 ** 31, res), 2 ** 31 - 1)
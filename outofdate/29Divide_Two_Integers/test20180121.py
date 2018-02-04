'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

#
def divide(self, dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)

#
def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        quotient = 0
        if ((dividend > 0 and divisor) > 0 or (dividend < 0 and divisor < 0)):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while (dividend >= divisor):
            k = 0
            temp = divisor
            while (dividend >= temp):
                dividend -= temp
                quotient += 1 << k
                temp <<= 1
                k += 1
        quotient *= sign
        if quotient > MAX_INT:
            return MAX_INT
        return quotient
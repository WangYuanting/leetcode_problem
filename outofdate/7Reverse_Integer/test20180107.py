'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x>0:
            str_x=str(x)
            list_x=list(str_x)
            list_x.reverse()
            rx=0
            for i in xrange(len(list_x)):
                rx=rx*10+int(list_x[i])
            if abs(rx) > 2147483647: return 0
            return rx
        elif x<0:
            str_x = str(-1*x)
            list_x = list(str_x)
            list_x.reverse()
            rx = 0
            for i in xrange(len(list_x)):
                rx = rx * 10 + int(list_x[i])
            if abs(rx) > 2147483647: return 0
            return rx*-1
        else:
            return 0
a=Solution()
b=a.reverse(123)
print b


def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    tmp = str(x)
    sign = ''
    overflow = 2 ** 31 - 1
    if tmp[0] == '-':
        sign = tmp[0]
        tmp = tmp[1:]
    res = tmp[::-1]
    for i in range(len(res)):
        if not res[i] == 0:
            break
    res = res[i:]
    res = int(sign + res)
    if abs(res) > overflow:
        return 0
    else:
        return res
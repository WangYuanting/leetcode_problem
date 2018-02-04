'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        if str=='':return 0
        rs=0
        number=['0','1','2','3','4','5','6','7','8','9']
        start=0
        if str[0]=='-' or str[0]=='+' :
            start=1
        for i in xrange(start,len(str)):
            if str[i]=='-' or str[i]=='+' :
                return 0
            if str[i] in number:
                rs=rs*10+int(str[i])
            else:
                break

        if str[0]=='-':
            if rs > 2147483648:
                rs = 2147483648
            return rs*-1
        else:
            if rs > 2147483647:
                rs = 2147483647
            return rs
a=Solution()
b=a.myAtoi("+-2")
print b


def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    # Check if Input String is null or of 0 length.
    str = str.strip()
    result = 0
    i = 0
    tmp = '0'

    if (len(str) == 0):
        return result

    if str[0] in "+-":
        tmp = str[0]
        i = 1
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    for i in range(i, len(str)):
        if str[i].isdigit():
            tmp += str[i]
        else:
            break

    if len(tmp) > 1:
        result = int(tmp)
    if result > MAX_INT > 0:
        return MAX_INT
    elif result < MIN_INT < 0:
        return MIN_INT
    else:
        return result
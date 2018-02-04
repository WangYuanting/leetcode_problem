'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length=len(s)
        if numRows==1 or length<=numRows:return s
        count = 2 * numRows - 2

        if length % (count) == 0:
            nl = length / (count)
        else:
            nl = length / (count) + 1
        r_str=''
        for i in xrange(numRows):
            for j in xrange(nl):
                if i==0 or i==numRows-1:
                    num_i=i+count*j
                    if num_i < length:
                        r_str += s[num_i]
                else:
                    num_i=i+count*j
                    if num_i < length:
                        r_str += s[num_i]
                        num_i=2*numRows-2-i + count * j
                        if num_i < length:
                            r_str += s[num_i]

        return r_str

a=Solution()
b=a.convert("PAYPALISHIRING", 4)
print b
c="PINALSIGYAHRPI"
print c


def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(L)
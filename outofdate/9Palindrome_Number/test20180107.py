'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        s=str(x)
        if len(s)==1:
            return True
        n=len(s)
        if n%2==0:
            for i in xrange(n/2):
                if s[i]!=s[n-1-i]:
                    return False
            return True
        else:
            for i in xrange(n/2):
                if s[i]!=s[n-1-i]:
                    return False
            return True


a=Solution()
b=a.isPalindrome(123521)
print b


def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    reverse = x[::-1]
    if x == reverse:
        return True
    return False
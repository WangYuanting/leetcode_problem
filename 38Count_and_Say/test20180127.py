'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        input='1'
        for i in xrange(n-1):
            input=self.count_one(input)
        return input
    def count_one(self,input):
        output=""
        temp=''
        times=0
        n=len(input)
        for i in xrange(n):
            in_=input[i]
            if temp=='':
                temp=in_
                times=1
            elif temp==in_:
                times+=1
            elif temp!=in_:
                output+=str(times)+temp
                temp=in_
                times=1
            if i == n - 1:
                output += str(times) + temp

        return output


#
class Solution1:
    # @return a string
    def count(self,s):
        t=''; count=0; curr='#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s
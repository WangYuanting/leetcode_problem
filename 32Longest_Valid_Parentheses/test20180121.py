'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        stk=[]
        lst=-1
        for i in xrange(len(s)):
            if s[i]=='(':
                if lst!=-1:
                    stk.append(lst)
                    lst=-1
                else:
                    stk.append(i)
            else:
                if stk:
                    stt=stk.pop()
                    if i-stt+1>result:
                        result=i-stt+1
                    lst=stt
                else:
                    lst=-1
        return result
#
def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
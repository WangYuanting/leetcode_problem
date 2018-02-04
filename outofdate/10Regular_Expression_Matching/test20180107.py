#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(p,s,0,0,False,False)


    def match(self,p,s,start_p,start_s,last_x,last_d):
        ns = len(s)
        np = len(p)
        is_x = self.find_x(p, start_p)
        is_d = self.find_d(p, start_p)
        if np==1:
            if p==u'.' and ns==1:return True
            elif p==s:return True
            else:
                return False
        elif np==2:
            if self.find_x(p,np-2):
                if self.find_d(p,np-2):
                    return True
                else:
                    if s[start_s:]==p[start_p]*(len(s[start_s:])):
                        return True
                    else:
                        return False
        elif len(p[start_p:])==1:
            if p[start_p:]==u'.' and len(s[start_s:])==1:return True
            elif p[start_p:]==s[start_s:]:return True
            else:
                return False
        elif len(p[start_p:])==2:
            if self.find_x(p,np-2):
                if self.find_d(p,np-2):
                    return True
                else:
                    if s[start_s:]==p[start_p]*(len(s[start_s:])):
                        return True
                    else:
                        return False

        if ns==start_s and np==start_p:
            return True
        elif ns <= start_s or np <= start_p:
            return False
        elif not is_x and not is_d :
            if s[start_s]==p[start_p]:
                return self.match(p,s,start_p+1,start_s+1,False,False)
            else:
                return False
        elif is_x and is_d:
            tof=False
            for i in xrange(start_s,ns):
                if self.match(p,s,start_p+2,i,True,True):
                    tof=True
                    return True
            if not tof:
                return False
        elif is_d and not is_x:
            return self.match(p,s,start_p+1,start_s+1,False,True)
        elif is_x and not is_d:
            tof=False
            for i in xrange(start_s,ns):
                if s[i]==p[start_p]:
                    tof= self.match(p,s,start_p+2,i,True,False)
                    if tof:
                        break
            return tof



    def find_x(self,p,start):
        if start+1>=len(p):
            return False
        elif u'*'==p[start+1]:
            return True
        else:
            return False

    def find_d(self, p, start):
        if start  >=len(p):
            return False
        elif u'.' == p[start]:
            return True
        else:
            return False


a=Solution()

'''

b=a.isMatch("aa", "a")
print b,False
b=a.isMatch("abcdede", "ab.*de")
print b,True
b=a.isMatch("aa", "a*")
print b,True
b=a.isMatch("aa", ".*")
print b,True
b=a.isMatch("abcd", "d*")
print b,False

b=a.isMatch("aaa", "ab*a")
print b,False

'''


b=a.isMatch("aab", "c*a*b")
print b,True



def _isMatch(self, s, p, s_index, p_index, cache):
    if (s_index, p_index) in cache:
        return cache[(s_index, p_index)]
    elif s_index == -1 and p_index == -1:
        return True
    elif p_index == -1 or s_index < -1:
        return False
    elif p[p_index] == '.':
        return self._isMatch(s, p, s_index - 1, p_index - 1, cache)
    if p[p_index] == '*' and p_index > 0:
        if p[p_index - 1] == '.' or (s_index >= 0 and p[p_index - 1] == s[s_index]):
            if self._isMatch(s, p, s_index - 1, p_index - 2, cache) or self._isMatch(s, p, s_index - 1, p_index, cache):
                return True
        if self._isMatch(s, p, s_index, p_index - 2, cache):
            return True
    elif s_index >= 0 and p[p_index] == s[s_index] and self._isMatch(s, p, s_index - 1, p_index - 1, cache):
        return True
    cache[(s_index, p_index)] = False
    return False


def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    return self._isMatch(s, p, len(s) - 1, len(p) - 1, {})

def isMatch1(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


def isMatch2(self, text, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]
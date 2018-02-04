'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':return 0
        if len(s)==1:return 1
        list=[]
        n=len(s)
        dis=[0,1]
        tof=True
        while True:
            if dis[1]==n:
                break
            temp_str=s[dis[0]:dis[1]]
            if tof:
                if dis[1]<n:
                    if s[dis[1]] in temp_str:

                        tof=False
                    else:
                        dis[1]+=1
                    list.append(dis[1] - dis[0])
                else:
                    break
            else:
                if dis[1]<n:
                    if s[dis[1]] in s[dis[0]+1:dis[1]]:
                        dis[0]+=1
                    else:
                        dis[0] += 1
                        dis[1]+=1
                        tof=True
        if list==[]:return len(s)
        return max(list)


a=Solution()
c=a.lengthOfLongestSubstring("aab")
print c


def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    ind = {}
    w = 0
    m = 0
    for i in range(0, len(s)):
        c = s[i]
        if i == 0:
            ind[c] = 1
            m = 1
        else:
            if c not in ind or ind[c] < w:
                ind[c] = i + 1
                d = i + 1 - w
                m = d if d > m else m
            else:
                w = ind[c]
                ind[c] = i + 1
    return m



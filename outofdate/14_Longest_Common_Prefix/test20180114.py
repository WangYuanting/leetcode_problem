'''
Write a function to find the longest common prefix string amongst an array of strings.


'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return u''
        elif len(strs)==1:
            return strs[0]
        elif u'' in strs:
            return u''
        temp_str=strs[0]
        temp_n=len(temp_str)
        n=0
        while n<=temp_n:
            tof=True
            for s in strs:
                if temp_str[:n]!=s[:n]:
                    tof=False
                    break
            if tof:
                n+=1
            else:
                break
        return temp_str[:n-1]

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if strs is not None and len(strs) > 0:
            strs.sort()
            a = strs[0]
            b = strs[len(strs) - 1]

            for i in range(len(a)):
                if len(b) > i and a[i] == b[i]:
                    res += b[i]
                else:
                    return res
        return res



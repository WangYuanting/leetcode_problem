'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words==[]:
            return []
        n=len(words[0])
        r=[]
        for w in words:
            i=self.f(r,s,n,w,-1)
            r.append(i)
        return r
    def f(self,r,s,n,w,start=-1):
        if start==-1:
            i=s.find(w,0)
        else:
            i = s.find(w, r[start]+n)
        if i==-1:
            return -1
        tof=True
        for r_i in r:
            if r_i<i<r_i+n:
                tof=False
        if tof:
            return i
        else:
            return self.f(r,s,n,w,start=start+1)

#
def _findSubstring(self, l, r, n, k, t, s, req, ans):
    curr = {}
    while r + k <= n:
        w = s[r:r + k]
        r += k
        if w not in req:
            l = r
            curr.clear()
        else:
            curr[w] = curr[w] + 1 if w in curr else 1
            while curr[w] > req[w]:
                curr[s[l:l + k]] -= 1
                l += k
            if r - l == t:
                ans.append(l)

def findSubstring(self, s, words):
    if not s or not words or not words[0]:
        return []
    n = len(s)
    k = len(words[0])
    t = len(words) * k
    req = {}
    for w in words:
        req[w] = req[w] + 1 if w in req else 1
    ans = []
    for i in xrange(min(k, n - t + 1)):
        self._findSubstring(i, i, n, k, t, s, req, ans)
    return ans




#
def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        s_len, w_len = len(s), len(words[0])
        w_len_total = len(words) * w_len
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        curr = {}
        res = []
        for start in range(w_len):
            curr = {}
            end = start
            while start + w_len_total <= s_len:
                sub = s[end:end + w_len]
                end += w_len
                if sub not in counter:
                    curr = {}
                    start = end
                else:
                    curr[sub] = curr.get(sub, 0) + 1
                    while curr[sub] > counter[sub]:
                        curr[s[start: start + w_len]] -= 1
                        start += w_len
                    if start + w_len_total == end:
                        res.append(start)
        return res
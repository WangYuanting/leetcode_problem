'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sort_nums=sorted(nums)
        count=0
        temp_num=u''
        reduce_nums=[]
        for i in sort_nums:
            if temp_num==u'':
                temp_num=i
                reduce_nums.append(i)
                count=1
            elif temp_num==i:
                count+=1
                reduce_nums.append(i)
                if count==3:
                    count=0
                    temp_num=u''
            else:
                reduce_nums.append(i)
                count = 0
                temp_num = u''

        temp_dict={}
        temp_list=[]
        n=len(nums)
        for i in xrange(n):
            for j in xrange(i+1,n):
                for k in xrange(j+1,n):
                    if reduce_nums[i]+reduce_nums[j]+reduce_nums[k]==0:
                        a=sorted([reduce_nums[i],reduce_nums[j],reduce_nums[k]])
                        if a not in temp_list:
                            temp_list.append(a)
        return temp_list


a=Solution()
b=[4,-10,-11,-12,-8,-12,-14,-11,-6,2,-4,2,3,12,-3,-12,-14,-12,-8,-9,-6,-3,10,2,14,10,7,-7,-9,0,-9,10,-2,-5,14,5,-9,7,9,0,-14,12,10,4,9,-8,8,11,-5,-15,-13,-3,-11,4,14,11,-1,-2,-11,5,14,-4,-8,-3,6,-9,9,12,6,3,-10,7,0,-15,-3,-13,-8,12,13,-5,12,-15,7,8,-4,-2,4,2,3,9,-8,2,-10,-1,6,3,-2,0,-7,11,-12,-2,3,-4,-2,7,-2,-3,4,-12,-1,1,10,13,-5,-9,-12,6,8,7,0,7,-6,5,13,8,-14,-12]
print len(b)

c=a.threeSum(b)
print c

def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        if 0 in counter and counter[0] > 2:
            res.append([0, 0, 0])

        pos = [p for p in counter if p > 0]
        neg = [n for n in counter if n < 0]

        for p in pos:
            for n in neg:
                r = -p - n
                if r in counter:
                    if (r == p or r == n) and counter[r] > 1:
                        res.append([n, r, p])
                    if r > p:
                        res.append([n, p, r])
                    if r < n:
                        res.append([r, n, p])
                    if r == 0:
                        res.append([n, 0, p])
        return res
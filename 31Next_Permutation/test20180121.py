#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:return
        if len(nums)==2:
            temp = nums[1]
            nums[1] = nums[0]
            nums[0] = temp
            return
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                continue
            else:
                break
        for j in xrange(i+1,len(nums),1):
            if nums[j]>nums[i]:
                continue
            else:
                break
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        self.reverse(nums,i+1)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def reverse(self,nums,start):
        end=len(nums)-1
        while start<end:
            self.swap(nums,start,end)
            start+=1
            end-=1

a=Solution()
b=a.nextPermutation([1,2,3])


def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Use two-pointers: two pointers start from back
    # first pointer j stop at descending point
    # second pointer i stop at value > nums[j]
    # swap and sort rest
    if not nums: return None
    i = len(nums) - 1
    j = -1  # j is set to -1 for case `4321`, so need to reverse all in following step
    while i > 0:
        if nums[i - 1] < nums[i]:  # first one violates the trend
            j = i - 1
            break
        i -= 1
    for i in xrange(len(nums) - 1, -1, -1):
        if nums[i] > nums[j]:  #
            nums[i], nums[j] = nums[j], nums[i]  # swap position
            nums[j + 1:] = sorted(nums[j + 1:])  # sort rest
            return
#
def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        i = len_ - 2
        change = False
        while i > -1:
            min = 2 ** 31 - 1
            index = -1
            for j in range(i + 1, len_):
                k = nums[j] - nums[i]
                if k <= min and k > 0:
                    index = j
                    min = k
            if index != -1:
                t = nums[index]
                nums[index] = nums[i]
                nums[i] = t
                change = True
                break
            i -= 1
        nums[i + 1:] = sorted(nums[i + 1:])
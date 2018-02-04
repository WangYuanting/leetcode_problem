'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:return 0
        temp=nums[0]
        r=1
        for i in xrange(len(nums)):
            if nums[i]!=temp:
                temp= nums[i]
                r+=1
        return r
a=Solution()
b=a.removeDuplicates([1,1,2])


def removeDuplicates(self, A):
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    return newTail + 1

#
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        if (L == 0):
            return 0

        ele = nums[0]
        ptr = 1
        for i in range(1, L):

            if (nums[i] == ele):
                continue
            else:
                ele = nums[i]
                nums[ptr] = ele
                ptr += 1

        return ptr

removeDuplicates(1,[1,1,2])
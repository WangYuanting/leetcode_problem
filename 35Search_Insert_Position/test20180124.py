'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        if r==-1:
            return 0
        elif nums[l]>target:
            return 0
        elif nums[r]<target:
            return r+1
        while l+1<r:
            mid = (l + r) / 2
            if target < nums[mid]:
                r = mid
            else:
                l = mid
        if nums[r]==target:
            return r
        elif nums[l]==target:
            return l
        elif nums[l]<target<nums[r]:
            return r

a=Solution()
b=a.searchInsert([1,3,5,6],5)


def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid
    return l
'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        low=0
        high=len(nums)-1
        while low<=high:
            if low+1==high:
                if nums[low]==target and nums[high]==target:
                    return [low,high]
                elif nums[low]<target and nums[high]==target:
                    return [high,high]
                elif nums[low]==target and nums[high]>target:
                    return [low,low]
                else:
                    return [-1,-1]
            mid=low+(high-low)*3/5
            type,temp_num=self.find_num(mid,nums,target)
            if type=='low':
                low=mid
            elif type=='high':
                high=mid
            elif type=='mid':
                low=self.find_low(low,mid,nums,target)
                high=self.find_high(mid,high,nums,target)
                break
        return [low,high]


    def find_num(self,mid,nums,target):
        if nums[mid]==target:
            return 'mid',mid
        elif nums[mid]<target:
            return 'low',mid
        elif nums[mid]>target:
            return 'high',mid
    def find_low(self,low,high,nums,target):
        if low==high:
            return low if nums[low]==target else -1
        elif nums[low]==target:
            return low
        elif low+1==high:
            return low if nums[low] == target else high
        mid = low + (high - low) * 3 / 5
        if nums[mid] == target:
            return self.find_low(low,mid,nums,target)
        elif nums[mid]<target:
            return self.find_low(mid,high,nums,target)
    def find_high(self,low,high,nums,target):
        if low==high:
            return low if nums[low]==target else -1
        elif nums[high]==target:
            return high
        elif low+1==high:
            return high if nums[high]==target else low
        mid = low + (high - low) * 3 / 5
        if nums[mid] == target:
            return self.find_high(mid,high,nums,target)
        elif nums[mid]>target:
            return self.find_high(low,mid,nums,target)

a=Solution()
b=a.searchRange([1,2,3,3,3,3,4,5,9],3)


def searchRange(self, nums, target):
    """
    :type nums: List[int] 1 2 2
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return [-1, -1]
    left = -1
    right = -1
    l = 0
    r = len(nums) - 1

    while l + 1 < r:
        mid = (l + r) / 2
        if target >= nums[mid]:
            l = mid
        else:
            r = mid
    if nums[l] == target:
        right = l
    if nums[r] == target:
        right = r

    l = 0
    r = len(nums) - 1
    while l + 1 < r:  # [5, 7, 7, 8, 8, 10]
        mid = (l + r) / 2
        if target > nums[mid]:
            l = mid
        else:
            r = mid
    if nums[r] == target:
        left = r
    if nums[l] == target:
        left = l

    if left > -1 and right > -1:
        return [left, right]
    elif left > -1:
        return [left, left]
    elif right > -1:
        return [right, right]
    else:
        return [-1, -1]


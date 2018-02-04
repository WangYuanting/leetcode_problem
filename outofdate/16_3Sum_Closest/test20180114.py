#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

a=Solution()
b=a.threeSumClosest([0,2,1,-3],1)
print(b)


def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    length = len(nums)
    if length <= 3:
        return sum(nums)
    nums = sorted(nums)
    minSum = nums[0] + nums[1] + nums[2]
    # if minimum of the sum greater than target
    if minSum >= target:
        return minSum

    maxSum = nums[-3] + nums[-2] + nums[-1]
    if maxSum <= target:
        return maxSum

    if target - minSum < maxSum - target:
        closest, distance = minSum, target - minSum
    else:
        closest, distance = maxSum, maxSum - target

    for i in range(length - 2):
        # skip if already checked
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        left, right = i + 1, length - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                return target
            dis = abs(target - s)

            # if get closer
            if dis < distance:
                closest, distance = s, dis
            elif s < target:
                # if max sum of current `left to right` less than target, exit
                if nums[i] + nums[right] * 2 < target:
                    break
                left += 1
            else:
                # if current min sum greater than target, exit
                if nums[i] + nums[left] * 2 > target:
                    break
                right -= 1
    return closest
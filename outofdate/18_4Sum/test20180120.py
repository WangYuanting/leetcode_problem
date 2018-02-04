'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(0,len(nums),1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(len(nums)-1,i,-1):
                if j<len(nums)-1 and nums[j] == nums[j+1]:
                    continue
                l,r=i+1,j-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]+nums[j]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[l], nums[r],nums[j]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1;
                        r -= 1
        return res

a=Solution()
b=a.fourSum([0,0,0,0],1)
print b


def binarySearch(self, nums, left, right, target):
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left


def fourSum(self, nums, target):
    n = len(nums)
    result = []
    snum = sorted(nums)
    # print snum
    if n == 0:
        return result
    if target > snum[n - 1] * 4 or target < snum[0] * 4:
        return result
    for i in xrange(n - 3):
        if i > 0 and snum[i] == snum[i - 1]:
            pass
            # print 'hello',i
        elif target < 4 * snum[i]:
            break
        else:
            if target - snum[i] > snum[n - 1] * 3:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and snum[j] == snum[j - 1]:
                    pass
                elif target - snum[i] - snum[j] > snum[n - 1] * 2:
                    continue
                elif target - snum[i] < snum[j] * 3:
                    break
                else:
                    # print i,j
                    k = j + 1
                    curTarget = target - snum[i] - snum[j]
                    if curTarget < snum[k] * 2:
                        break
                    index = self.binarySearch(snum, k + 1, n - 1, curTarget - snum[k])
                    if index == n:
                        index -= 1
                    while (k < index):
                        if snum[k] + snum[index] == curTarget:
                            # print i,j,k,index
                            result.append([snum[i], snum[j], snum[k], snum[index]])
                            while index > 0 and snum[index - 1] == snum[index]:
                                index -= 1
                            index -= 1
                            while k < n - 1 and snum[k] == snum[k + 1]:
                                k += 1
                            k += 1
                        elif snum[k] + snum[index] < curTarget:
                            k += 1
                        else:
                            index -= 1
    return result
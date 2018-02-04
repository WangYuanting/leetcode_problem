'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp_can=[]
        for i in candidates:
            if i not in temp_can:
                temp_can.append(i)
        can=sorted(temp_can,reverse=True)


        print(can)
    def count_target(self,can,target):
        aim_dict=dict()

        output_list=[]
        remain=target
        start=0
        while start<len(can):
            if can[start]<=remain:
                output_list.append(can[start])
                remain-=can[start]
            elif can[start]>remain:
                start+=1


        if can[start]<=target:
            return start
    def count_poss(self,aim_dict,can,input_list,target):
        pass


a=Solution()
b=a.combinationSum([2,3,6,7],7)


def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in xrange(index, len(nums)):
        self.dfs(nums, target - nums[i], i, path + [nums[i]], res)
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        _path = []
        candidates.sort()  # sort the candidate values
        pos = 0
        self.dfs(candidates, target, pos, _path, res)
        return res

    def dfs(self, candidates, target, pos, _path, res):
        if (target == 0):
            res.append(_path[:])
            return

        while (pos < len(candidates) and candidates[pos] <= target):
            _path.append(candidates[pos])
            self.dfs(candidates, target - candidates[pos], pos, _path, res)
            _path.pop()  # backtrack
            pos += 1
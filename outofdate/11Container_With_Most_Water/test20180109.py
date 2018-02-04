'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        for i in xrange(len(height)):
            for j in xrange(i+1,len(height)):
                temp=min(height[i],height[j])*(j-i)
                if max<temp:
                    max=temp
        return max

def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ans = -1
        while l != r:
            x = height[l]
            y = height[r]
            if x > y:
                if (r - l) * y > ans:
                    ans = (r - l) * y
                r -= 1
                while l != r:

                    if height[r] <= y:
                        r -= 1
                    else:
                        break

            else:
                if (r - l) * x > ans:
                    ans = (r - l) * x
                l += 1
                while l != r:
                    if height[l] <= x:
                        l += 1
                    else:
                        break
        return ans


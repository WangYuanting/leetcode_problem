'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        max1=len(nums1)
        max2=len(nums2)
        n1=0
        n2=0
        list=[]
        if nums1==[]:
            list=nums2
        elif nums2==[]:
            list=nums1
        else:
            while True:
                if n1==max1:
                    for i in xrange(n2,max2):
                        list.append(nums2[i])
                    break
                elif n2==max2:
                    for i in xrange(n1,max1):
                        list.append(nums1[i])
                    break
                elif nums1[n1]<nums2[n2]:
                    list.append(nums1[n1])
                    n1+=1
                else:
                    list.append(nums2[n2])
                    n2 += 1

        n=len(list)
        if n%2==0:
            return (list[n/2-1]+list[n/2])/float(2)
        else:
            return list[(n-1)/2]

a=Solution()
b=a.findMedianSortedArrays([],[2,3])
print b


def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    all_nums = nums1 + nums2
    len_all = len(all_nums)
    all_nums.sort()

    if len_all == 0:
        return None
    elif len_all == 1:
        return all_nums[0]
    elif len_all == 2:
        return ((all_nums[0] + all_nums[1]) / 2.0)

    if len_all % 2 == 0:
        median = (all_nums[(len(all_nums) / 2)] + all_nums[(len(all_nums) / 2) - 1]) / 2.0
    else:
        median = all_nums[(len(all_nums) / 2)]

    return median
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
import sys
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        s = t = ListNode(0)
        while not (lists==[] or set(lists)=={None}):
            min=sys.maxint
            for l in lists:
                if l.val<min:
                    temp=l
                    min=l.val
            t.next=temp
            temp=temp.next
            t = t.next
        return s.next
a=Solution()
b=a.mergeKLists([ListNode(1)])


def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    self.nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            self.nodes.append(l.val)
            l = l.next
    for x in sorted(self.nodes):
        point.next = ListNode(x)
        point = point.next
    return head.next


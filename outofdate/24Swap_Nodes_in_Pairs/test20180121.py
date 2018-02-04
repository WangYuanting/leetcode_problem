'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def swapPairs(self, head):
        p1 = guard = ListNode(0)
        guard.next = head

        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1
        except:
            return guard.next

#
def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head
        nn = None
        while head:
            if head.next:
                nn = head.next
            else:
                return dummy_head.next
            head.next = nn.next
            prev.next = nn
            nn.next = head

            prev = head
            head = head.next
        return dummy_head.next
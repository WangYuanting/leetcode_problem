'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None and n==1:return []
        temp_next = head.next
        if n==1:return temp_next
        i=2
        while i<n:
            temp_next=temp_next.next
            i+=1
        temp_next.next=None if temp_next==None else temp_next.next
        return head
a=ListNode(1)
a.next=ListNode(2)

s=Solution()
b=s.removeNthFromEnd(a,2)
print b


def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if not head:
        return head

    dummy = ListNode
    dummy.next = head

    fast = head

    while n:
        fast = fast.next
        n -= 1

    if not fast:
        return head.next

    fast = fast.next

    while fast:
        head = head.next
        fast = fast.next

    head.next = head.next.next

    return dummy.next
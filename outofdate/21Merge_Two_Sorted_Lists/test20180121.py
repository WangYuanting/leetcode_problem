'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        First=ListNode
        temp=First
        temp1=l1
        temp2=l2
        while True:
            if temp1!=None:
                temp.next=ListNode(temp1.val)
                temp=temp.next
                temp1=temp1.next
            if temp2!=None:
                temp.next = ListNode(temp2.val)
                temp = temp.next
                temp2=temp2.next
            if temp1==None and temp2==None:break
        return First.next
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
#
def mergeTwoLists(self, l1, l2):
    """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
    """
    s = t = ListNode(0)
    if (l1 == None and l2 == None):
        t.next = None
    elif (l1 == None):
        t.next = l2
    elif (l2 == None):
        t.next = l1
    else:
        while not (l1 is None or l2 is None):
            if l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        t.next = l1 or l2
    return s.next
'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1_1=ListNode(3)
l1_2=ListNode(8)
l1_2.next=None
l1=ListNode(1)
l1.next=l1_2
#l1=ListNode(5)


l2_1=ListNode(4)
l2_2=ListNode(6)
#l2_2.next=l2_1
l2_2.next=None
l2=ListNode(5)
l2.next=l2_2
l2=ListNode(0)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #r_l= self.sum_list(None,l1,l2)
        #return self.re_node(r_l,None)
        ll1=self.node_list(l1,[])
        ll1.reverse()
        ll2 = self.node_list(l2, [])
        ll2.reverse()
        sll1=0
        for i in xrange(len(ll1)):
            sll1=sll1*10+ll1[i]
        sll2= 0
        for i in xrange(len(ll2)):
            sll2= sll2 * 10 + ll2[i]
        s=sll1+sll2
        l_r=self.list_node(None,list(str(s)))
        return l_r
    def list_node(self,node,list):
        if len(list)==0:
            return node
        a=ListNode(list[0])
        a.next=node
        list=list[1:]
        return self.list_node(a,list)



    def node_list(self,node,list):
        list.append(node.val)

        if node.next==None:
            return list
        else:
            return self.node_list(node.next,list)



    def re_node(self,r_l,re):
        if r_l==None:
            return re
        a=ListNode(r_l.val)
        a.next=re
        return self.re_node(r_l.next,a)

    def sum_list(self,temp_node,l1,l2):
        if l1==None:
            if l2==None:
                return temp_node
            else:
                if temp_node.val<10:
                    a=ListNode(l2.val)
                    a.next=temp_node
                else:
                    temp_node.val=temp_node.val-10
                    a = ListNode(l2.val+1)
                    a.next = temp_node
        else:
            if l2==None:
                if temp_node.val<10:
                    a=ListNode(l1.val)
                    a.next=temp_node
                else:
                    temp_node.val=temp_node.val-10
                    a = ListNode(l1.val+1)
                    a.next = temp_node
            else:
                if temp_node==None:
                    m=l2.val + l1.val
                    if m<10:
                        a = ListNode(l2.val + l1.val)
                    else:
                        a=ListNode(1)
                        b=ListNode(m-10)
                        a.next=b
                elif temp_node.val<10:
                    a=ListNode(l2.val+l1.val)
                    a.next=temp_node
                else:
                    temp_node.val=temp_node.val-10
                    a = ListNode(l2.val+l1.val+1)
                    a.next = temp_node

        if l1.next==None :
            if l2.next==None :
                return a
            else:
                return self.sum_list(a, l2.next, ListNode(0))
        else:
            if l2.next==None :
                return self.sum_list(a, l1.next, ListNode(0))
            else:
                return self.sum_list(a, l1.next, l2.next)



a=Solution()
b=a.addTwoNumbers(l1,l2)
while b!=None:
    print b.val
    b=b.next





def addTwoNumbers(self, l1, l2):
    helper, e = ListNode(0), 0
    helper_copy = helper
    while l1 or l2 or e:
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        new_node = ListNode((l1_value + l2_value + e) % 10)
        e = (l1_value + l2_value + e) // 10
        helper.next = new_node
        helper = helper.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return helper_copy.next
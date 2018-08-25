'''
21 Merge Two Sorted List:

简单

简单但很基础的链表操作，合并两个排过序的链表


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

        if None == l1:
            return l2

        if None == l2:
            return l1

        head = ''
        cur = ''

        pt1 = l1
        pt2 = l2

        if pt1.val >= pt2.val:
            head = pt2
            pt2 = pt2.next
        else:
            head = pt1
            pt1 = pt1.next
        cur = head
        cur.next = None

        while True:

            if None == pt1:
                cur.next = pt2
                break
            if None == pt2:
                cur.next = pt1
                break

            if pt2.val >= pt1.val:
                cur.next = pt1
                pt1 = pt1.next
            else:
                cur.next = pt2
                pt2 = pt2.next
            cur = cur.next
            cur.next = None

        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)

t1 = l1
l1.next = l2
l2.next = l3

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)

t2 = l4
l4.next = l5
l5.next = l6


c = Solution()
d = c.mergeTwoLists(t1, t2)
while True:

    if None == d:

        break
    print(d.val)
    d = d.next




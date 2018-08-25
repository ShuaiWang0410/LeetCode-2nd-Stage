'''
Problem 24:

反转节点

将一个链表上每相邻的两个节点进行反转


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if None == head:
            return None

        pt1 = head
        pt2 = head.next
        rpt = head
        n_head = ''
        start_flag = False

        if None == pt2:
            return head


        while True:

            if pt2.next != None:
                pt1.next = pt2.next
            else:
                pt1.next = None
            pt2.next = pt1

            if not start_flag:
                n_head = pt2
                start_flag = True
            else:
                rpt.next = pt2
                rpt = pt1

            if not pt1.next:
                break
            pt1 = pt1.next
            if not pt1.next:
                break
            pt2 = pt1.next


        return n_head

l1 = ListNode(1)
l2 = ListNode(2)
'''
l3 = ListNode(4)

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
'''
t1 = l1
l1.next = l2
'''
l2.next = l3

l3.next = l4
l4.next = l5
l5.next = l6
'''

c = Solution()
d = c.swapPairs(t1)

print("--")
while d != None:
    print(d.val)
    d = d.next

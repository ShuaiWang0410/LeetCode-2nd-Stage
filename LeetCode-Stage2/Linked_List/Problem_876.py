'''
876. Middle of the Linked List

Ace it

自己想出的简单方法，用两个速度不同的指针

第一个一倍速前进，第二个二倍速前进

当第二个到达列表尾部，那么第一个一定在中间

同理用不同倍速的可获得1/3,1/4,1/5处的指针

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p1 = head
        p2 = head

        while True:

            if p2.next != None:
                p2 = p2.next
            else:
                return p1

            p1 = p1.next

            if p2.next != None:
                p2 = p2.next
            if p2.next == None:
                return p1


'''
141. Linked List Cycle

How to detect a Cycle in a Linked list?


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if None == head:
            return False

        p1 = head
        p2 = head

        while True:

            if p2 != None:
                p2 = p2.next
            else:
                return False

            if p1 == p2:
                return True

            p1 = p1.next

            if p2 != None:
                p2 = p2.next
            else:
                return False


l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)
l4 = ListNode(1)



c = Solution()
print(c.hasCycle(None))
'''
142. Linked List Cycle II

Deepin of 141

Fellow


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dict = {}
        if None == head:
            return None

        cur = head
        dict[cur] = 1

        while True:
            if None == cur.next:
                return None

            cur = cur.next

            try:
                if 1 == dict[cur]:
                    return cur
            except KeyError:
                dict[cur] = 1

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2



c = Solution()
d = c.detectCycle(l1)
print(d.val)
'''
61. Rotate List

旋转链表，首先首尾相连
但是这题是倒着旋转，也就是与链表的连接方向相反

正转（t = t.next）是最方便的
因此可以首先缩减周期，将反转的次数缩减到1个周期
然后用周期数-反转数 = 正转数 来正转


'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if None == head:
            return head
        cur = head
        l_link = 1

        while True:

            if None == cur.next:
                break
            cur = cur.next
            l_link += 1

        cur.next = head
        move = head
        k = k % l_link

        for i in range(l_link - (k+1)):
            move = move.next

        n_head = move.next
        move.next = None
        return n_head

d1 = ListNode(0)
d2 = ListNode(1)

d1.next = d2
d2.next = d3

c = Solution()
d = c.rotateRight(d1, 4)
while d != None:
    print(d.val)
    d = d.next




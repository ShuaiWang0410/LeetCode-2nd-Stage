'''
Problem 83


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if None == head:
            return None

        cur = head
        last_val = cur.val
        last = cur
        cur = cur.next

        while None != cur:


            if last_val != cur.val:
                last_val = cur.val
                last = cur
                cur = cur.next
            else:
                last.next = cur.next
                cur = cur.next

        return head

s = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)

s.next = s2
s2.next = s3

c = Solution()
d = c.deleteDuplicates(s)

while True:
    if None == d:
        break
    else:
        print(d.val)
        d = d.next



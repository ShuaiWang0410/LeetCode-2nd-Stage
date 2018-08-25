'''



'''


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if None == head:
            return None

        node_dic = {}

        new_node = head

        while True:

            if None == new_node:
                break
            node_dic[id(new_node)] = RandomListNode(new_node.label)
            new_node = new_node.next

        new_head = node_dic[id(head)]
        link = head.next
        random = head
        new_link = new_head

        while True:

            if None == link:
                if None != random.random:
                    new_link.random = node_dic[id(random.random)]
                break

            new_link.next = node_dic[id(link)]
            if None != random.random:
                new_link.random = node_dic[id(random.random)]

            link = link.next
            random = random.next
            new_link = new_link.next

        return new_head

link1 = RandomListNode(-1)
link2 = RandomListNode(-1)
link1.next = link2
link1.random = link1
link2.random = link1
c = Solution()
d = c.copyRandomList(link1)
print(d)










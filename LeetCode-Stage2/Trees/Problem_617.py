'''
617. Merge Two Binary Trees

Ace it

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

将两棵二叉树的各个同位节点相加，如果有不同节点则进行扩展

需要两个指针进行便利

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if None != t1:

            temp1 = None
            temp2 = None

            if None != t2:
                temp1 = t2.left
                temp2 = t2.right
                t1.val += t2.val

            tc1 = self.mergeTrees(t1.left, temp1)
            tc2 = self.mergeTrees(t1.right, temp2)

            t1.left = tc1
            t1.right = tc2
            return t1


        else:

            if None != t2:

                tc1 = self.mergeTrees(None, t2.left)
                tc2 = self.mergeTrees(None, t2.right)
                t2.left = tc1
                t2.right = tc2

                return t2

            else:
                return None






'''
55. Jump Game

倒着来
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        l_nums = len(nums)
        if l_nums == 1 and nums[0] == 0:
            return False
        t = 0
        for i in range(l_nums - 2, -1, -1):
            t -= 1
            if nums[i] + t >= 0:
                t = 0
        if t == 0:
            return True
        return False
c = Solution()
print(c.canJump([2,0,3,1,0,4]))
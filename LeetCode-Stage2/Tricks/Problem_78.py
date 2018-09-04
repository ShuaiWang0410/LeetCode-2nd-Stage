'''
78. Subsets

给一个集合，输出它所有的subset
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sets = []
        l_nums = len(nums)

        sets.append([])

        for i in range(l_nums):
            tsets = []
            for j in sets:
                tsets.append(j + [nums[i]])
            sets += tsets

        return sets

c = Solution()
d = c.subsets([])
print(len(d))








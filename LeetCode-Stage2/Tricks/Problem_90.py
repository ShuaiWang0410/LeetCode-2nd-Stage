'''
90. Subsets II

Deepin of Problem 78

这次的集合中元素有duplicate，但不能输出duplicate

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        sets = []
        sets.append([])
        last = ''
        dup_end = -1

        for i in nums:
            if last == i:
                l = len(sets)
                tsets = []
                for j in sets[dup_end:]:
                    tsets.append(j + [i])
                sets += tsets
                dup_end = l
            else:
                dup_end = len(sets)
                tsets = []
                for j in sets:
                    tsets.append(j + [i])
                sets += tsets
                last = i
        return sets

c = Solution()
print(c.subsetsWithDup([]))






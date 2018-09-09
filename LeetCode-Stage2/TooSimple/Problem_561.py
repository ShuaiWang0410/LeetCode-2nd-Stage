'''
561. Array Partition I

'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sums = 0
        k = 0
        for i in nums:
            if 0 == k % 2:
                sums += i
            k += 1
        return sums
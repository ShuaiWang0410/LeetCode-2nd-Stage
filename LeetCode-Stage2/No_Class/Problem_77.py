'''
77. Combinations
输入n与k，n表示从1到n的数字，k表示组合数，输出所有的组合数

'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []

        sets = []
        pattern = [0 for i in range(n)]




    def combineR(self, sets, pattern, numbers, k):






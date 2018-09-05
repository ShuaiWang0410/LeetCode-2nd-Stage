'''
64. Minimum Path Sum

经典的地图动规题目

Deepin of 63


'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        l_row = len(grid)
        if 1 == l_row:
            return sum(grid[0])

        l_col = len(grid[0])

        row1 = [0 for i in range(l_col)]
        row2 = [0 for i in range(l_col)]

        row1[0] = grid[0][0]
        for i in range(1, l_col):
            row1[i] = row1[i - 1] + grid[0][i]

        for i in range(1, l_row):
            row2[0] = row1[0] + grid[i][0]

            for j in range(1, l_col):
                row2[j] = min(row2[j-1], row1[j]) + grid[i][j]

            temp = row1
            row1 = row2
            row2 = temp

        return row1[-1]

d = [
  [1]
]

c = Solution()
print(c.minPathSum(d))





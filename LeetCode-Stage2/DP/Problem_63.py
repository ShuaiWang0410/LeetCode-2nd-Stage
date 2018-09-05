'''
63. Unique Paths II

Deepin of 62

'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        l_row = len(obstacleGrid)
        if 1 == l_row:
            for i in obstacleGrid[0]:
                if 0 != i:
                    return 0
            return 1
        l_col = len(obstacleGrid[0])

        row1 = [0 for i in range(l_col)]
        row2 = [0 for i in range(l_col)]

        if 0 != obstacleGrid[0][0]:
            return 0

        row1[0] = 1

        for i in range(1, l_col):
            if 0 != obstacleGrid[0][i]:
                continue
            row1[i] = obstacleGrid[0][i] + row1[i-1]


        for i in range(1, l_row):

            row2[0] = row1[0]
            if 0 != obstacleGrid[i][0]:
                row2[0] = 0

            for j in range(1, l_col):
                if 0 != obstacleGrid[i][j]:
                    row2[j] = 0
                    continue
                row2[j] = row2[j - 1] + row1[j]

            temp = row1
            row1 = row2
            row2 = temp

        return row1[-1]

g = [
  [0]
]
c = Solution()
print(c.uniquePathsWithObstacles(g))



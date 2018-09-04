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

        for i in range(l_row):
            for j in range(l_col):
                if 



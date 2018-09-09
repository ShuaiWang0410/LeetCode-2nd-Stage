'''
883. Projection Area of 3D Shapes

'''


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        z = 0

        row = len(grid)
        col = len(grid[0])

        m_rows = [0 for i in range(row)]
        m_cols = [0 for i in range(col)]

        for i in range(row):
            for j in range(col):
                temp = grid[i][j]
                if 0 != temp:
                    z += 1
                if temp > m_rows[i]:
                    m_rows[i] = temp
                if temp > m_cols[j]:
                    m_cols[j] = temp
        return z + sum(m_rows) + sum(m_cols)
'''
74 Search a 2D matrix

在矩阵中，找到target，如果存在返回true，否则返回false

其中矩阵每行首元素都比上一行最后一个元素大
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if [] == matrix:
            return False

        m_row = len(matrix)
        m_col = len(matrix[0])

        if 0 == m_col:
            return False

        row = self.searchMatrixB(-1, 0, 0, m_row - 1, matrix, target)

        if -1 == row:
            return False

        if target == matrix[row][0]:
            return True

        return self.searchMatrixB(row, -1, 0, m_col - 1, matrix, target)




    def searchMatrixB(self, row, col, start, end, matrix, target):

        if row == -1:

            while True:

                if start > end:
                    return end

                mid = (start + end) // 2

                if target == matrix[mid][0]:
                    return mid
                elif target > matrix[mid][0]:
                    start = mid + 1
                    continue
                else:
                    end = mid - 1
                    continue
        else:

            while True:

                if start > end:
                    return False

                mid = (start + end) // 2

                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    start = mid + 1
                    continue
                else:
                    end = mid - 1
                    continue

m = [
  [2,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
c = Solution()
print(c.searchMatrix(m,50))







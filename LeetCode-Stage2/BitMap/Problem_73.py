'''
73. Set Matrix Zeroes

Hint

这个题要求找到m*n矩阵中所有的0，然后把它所在的行和列所有元素变成0

首先当然是两遍扫描，找到所有0，这里有一个简化，我们只需要记住变成0的行数和列数，并不需要记住每个点的坐标

这样就至少需要两个数组，一个长为m，另一个为n，空间复杂度m*n，用0表示不是0，1表示是0

但其实我们只需要两个数，用bitmap来表示这两个数组，这样一下子就变成了常数空间


'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        bit_row = 0
        bit_col = 0

        l_row = len(matrix)
        l_col = len(matrix[0])


        for i in range(l_row):

            for j in range(l_col):

                if 0 == matrix[i][j]:
                    bit_row |= 1 << i
                    bit_col |= 1 << j

        for i in range(l_row):

            last_row = bit_row
            bit_row >>= 1
            flag = 0
            if last_row > (bit_row << 1):
                flag = 1
            tbit_col = bit_col
            for j in range(l_col):
                if 1 == flag:
                    matrix[i][j] = 0
                    continue
                last_col = tbit_col
                tbit_col >>= 1
                if last_col > (tbit_col << 1):
                    matrix[i][j] = 0
m = [
  [1],
  [0],
  [1]
]
c = Solution()
c.setZeroes(m)
print(m)










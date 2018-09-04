'''
48. Rotate Image

递归旋转矩阵，从内到外，一层一层

'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        l_matrix = len(matrix)

        self.rotateR(0, l_matrix - 1, matrix)

    def rotateR(self, start, end, matrix):

        if end - start <= 0:
            return

        self.rotateR(start + 1, end - 1, matrix)
        m = start
        n = end
        points = [[start, start], [end, start], [end, end], [start, end]]
        move = [[0, 1],[-1,0],[0, -1],[1,0]]

        for i in range(start, end):

            temp = matrix[points[0][0]][points[0][1]]
            for j in range(1,4):
                matrix[points[j-1][0]][points[j-1][1]] = matrix[points[j][0]][points[j][1]]

            matrix[points[3][0]][points[3][1]] = temp
            for j in range(4):
                points[j][0] += move[j][0]
                points[j][1] += move[j][1]



c = Solution()
d = [
  [1,2],
  [3,4]
]
c.rotate(d)
for i in d:
    print(i)









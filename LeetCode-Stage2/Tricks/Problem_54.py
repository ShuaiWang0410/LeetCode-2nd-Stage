'''
54 Spiral Matrix

Deepin of 48

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        l_x = len(matrix)
        if 1 == l_x:
            return matrix[0]
        l_y = len(matrix[0])
        answer = []
        if 1 == l_y:
            for i in matrix:
                answer.append(i[0])
            return answer

        self.spiralOrderR(matrix, 0,0, l_x - 1, l_y - 1, answer)
        return answer


    def spiralOrderR(self, matrix, start_x, start_y, dig_x, dig_y, answer_set):

        if start_x > dig_x or dig_y < start_y:
            return

        dis_x = dig_x - start_x
        dis_y = dig_y - start_y

        if 0 == dis_x:
            s_y = start_y
            for i in range(dis_y + 1):
                answer_set.append(matrix[start_x][s_y])
                s_y += 1
            return
        if 0 == dis_y:
            s_x = start_x
            for i in range(dis_x + 1):
                answer_set.append(matrix[s_x][start_y])
                s_x += 1
            return



        start_points = [[start_x, start_y], [start_x, dig_y], [dig_x, dig_y], [dig_x, start_y]]
        move = [[0,1], [1,0], [0, -1], [-1,0]]
        dis = [dis_y, dis_x, dis_y, dis_x]

        for i in range(4):

            dist = dis[i]
            s_x = start_points[i][0]
            s_y = start_points[i][1]
            m_x = move[i][0]
            m_y = move[i][1]
            for i in range(dist):
                answer_set.append(matrix[s_x][s_y])
                s_x += m_x
                s_y += m_y

        self.spiralOrderR(matrix, start_x + 1, start_y + 1, dig_x - 1, dig_y - 1, answer_set)

c = Solution()
matrix = [
    [1],
    [10],
    [9]
]
print(c.spiralOrder(matrix))

matrix = [
    [1,2],
    [4,3]
]
print(c.spiralOrder(matrix))
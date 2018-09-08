'''
119 Pascal's Triangle II

Deepin of Problem 118

只输出三角形的第K行，但要求使用O(k)空间

'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex <= 0:
            return [1]


        row = [1,1]

        offset = 1
        for i in range(rowIndex - 1):

            l_row = len(row)
            temp1 = row[0]
            for j in range(l_row - 1):
                n = j + offset
                temp2 = row[n]
                row[n] = temp1 + row[n]
                temp1 = temp2
            row.append(1)

        return row

c = Solution()
print(c.getRow(1))


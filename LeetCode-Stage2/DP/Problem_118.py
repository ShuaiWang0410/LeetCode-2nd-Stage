'''
118. Pascal's Triangle

简单的构建三角形


'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if 0 == numRows:
            return []

        tri = [[1]]

        for i in range(1, numRows):
            row = []
            row.append(1)
            l = len(tri[-1])
            lrow = tri[-1]
            if l >= 2:
                for j in range(l - 1):
                    row.append(lrow[j] + lrow[j + 1])

            row.append(1)
            tri.append(row)



        return tri

c = Solution()
d = c.generate(3)
for i in d:
    print(i)
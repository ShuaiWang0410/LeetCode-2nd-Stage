'''




'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if [] == matrix or [] == matrix[0]:
            return 0
        if ["1"] == matrix[0]:
            return 1


        h = len(matrix[0])
        w = len(matrix)
        dp = [[0 for i in range(h)] for j in range(w)]
        length = 0

        for i in range(h):
            dp[0][i] = ord(matrix[0][i]) - ord("0")
        for i in range(w):
            dp[i][0] = ord(matrix[i][0]) - ord("0")

        for i in range(w):
            for j in range(h):

                if 0 == ord(matrix[i][j]) - ord("0"):
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    if length < dp[i][j]:
                        length = dp[i][j]

        if length > min(h,w):
            length = min(h,w)
        return length * length


c = Solution()
d = c.maximalSquare([["1"]])
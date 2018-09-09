class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        r_a = len(A)
        c_a = len(A[0])

        for i in range(r_a):
            for j in range(c_a):
                A[i][j] = 1 - A[i][j]
            A[i] = A[i][::-1]
        return A
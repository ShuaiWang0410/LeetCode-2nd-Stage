'''
62. Unique Paths

假设有一个m列n行的棋盘，左上为0，0，右下为m,n
小机器人从左上到达右下共有多少种走法？

比如一个1*2的表格，小机器人只能向下走，故只有1种走法
比如一个2*1的表格，小机器人只能横着走，故只有2种走法
一个2*2的表格，小机器人在到达原来的两个终点后，每个终点可以有一种方法走向新的终点，所以是之和

因此动态规划转移式是dp[i][j] = 1 when i == 0 or j == 0
                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
                 然而由于查找的方式特殊，故可以将状态由一个i*j棋盘压缩为两个横行不停地交换




'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if 0 == m or 0 == n:
            return 0

        if 1 == m or 1 == n:
            return 1

        dp1 = [1 for i in range(m)]
        dp2 = [1] + [0 for i in range(m - 1)]

        for i in range(n-1):

            for j in range(1, m):

                dp2[j] = dp2[j - 1] + dp1[j]

            temp = dp2
            dp2 = dp1
            dp1 = temp

        if n % 2 == 0:
            temp = dp2
            dp2 = dp1
            dp1 = temp
            return dp2[m-1]

        return dp1[m-1]








c = Solution()
print(c.uniquePaths(7,3))





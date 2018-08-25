class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for i in range(n + 1)]
        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2

        for i in range(1, n + 1):
            maxVal = i

            if n > 3:
                k = i // 2
                for j in range(1,k + 1):
                    temp = dp[j] * dp[i-j]
                    if temp > maxVal:
                        maxVal = temp
            else:
                dp[i] = max(dp[i],maxVal)
            dp[i] = maxVal

        return dp[n]

c = Solution()
print(c.integerBreak(5))







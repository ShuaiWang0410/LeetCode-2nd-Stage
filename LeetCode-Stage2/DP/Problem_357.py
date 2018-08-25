'''
357. Count Numbers with Unique Digits

给出n，计算0 - 10^n（包括0）中不含重复数字的个数
比如0-100中，有91个，其中11，22，33，44，55，66，77----99不是

思路，用动态规划，dp[n]表示10的n次方中unique的个数

2是100, 那么3是1000，1000中的重复个数为100个中的加一位，比如99，可以是199，919和991


'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            if 2 == n:
                return pow(10,2) - 9
            else:
                return 1

        dp = [0 for i in range(n + 1)]
        dp[2] = 9
        for i in range(3, n + 1):
            dp[i] = 1 + dp[i-1]*(i-1)*10 + dp[i - 1]*9
        return pow(10,n) - dp[n]

c = Solution()
print(c.countNumbersWithUniqueDigits(4))



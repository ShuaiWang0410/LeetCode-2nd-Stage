'''
29 Devide two Integers

Given the dividend and divisor,

不能使用除，余数和乘法，

'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if 0 == dividend:
            return 0

        if 1 == divisor:
            return dividend

        neg_flag = False
        if 0 > dividend * divisor:
            if -1 == divisor:
                return -dividend

            neg_flag = True
            dividend = -dividend


        times = 0
        while True:
            if 0 == dividend or abs(dividend) < abs(divisor):
                if neg_flag:
                    return -times
                return times
            dividend -= divisor
            times += 1

c = Solution()
print(c.divide(0,-3))
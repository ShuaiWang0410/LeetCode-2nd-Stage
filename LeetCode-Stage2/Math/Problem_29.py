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

        max = 2147483647
        nmax = -2147483648
        if 0 == dividend:
            return 0

        if 1 == divisor:
            if dividend > max or dividend < nmax:
                return max
            return dividend

        if -1 == divisor:
            if dividend > max + 1 or dividend <= nmax:
                return max
            return -dividend


        neg_flag = False
        if 0 > dividend * divisor:

            neg_flag = True
            if dividend < 0:
                dividend = -dividend
            if divisor < 0:
                divisor = -divisor
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        t_divisor = divisor
        result = 0
        t = 0
        while True:

            if dividend < t_divisor and t == 0:
                break

            if dividend > t_divisor:
                t_divisor <<= 1
                t += 1
            else:
                if dividend < t_divisor:
                    t -= 1
                    t_divisor >>= 1
                    result += pow(2,t)
                    dividend -= t_divisor
                    t_divisor = divisor
                    t = 0
                else:
                    result += pow(2,t)
                    break


        if neg_flag:
            if -result < nmax:
                return max
            return -result
        if result > max:
            return max
        return result











c = Solution()
print(c.divide(-2147483648,-1))
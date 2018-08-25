'''
13 RomanToInt

用栈

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {
            "I":1,
            "V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000}
        s_length = len(s)

        if s_length == 0:
            return 0
        if s_length == 1:
            return dic[s[0]]

        stack = [0 for i in range(s_length + 1)]

        stack[0] = 1145141919810
        head = 1
        num = 0
        cur = 0

        while True:

            if cur == s_length:
                break

            n = dic[s[cur]]
            if n <= stack[head - 1]:
                stack[head] = n
                head += 1
                num += n
            else:
                temp = n
                while True:
                    if stack[head - 1] >= n:
                        break

                    temp -= stack[head - 1]
                    num -= stack[head - 1]
                    head -= 1

                stack[head] = n
                head += 1
                num += temp


            cur += 1
        return num

c = Solution()
print(c.romanToInt("LVIII"))




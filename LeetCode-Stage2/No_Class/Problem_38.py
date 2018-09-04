'''
38 Count and Say:


'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 0:
            return ''

        if 1 == n:
            return '1'

        if 2 == n:
            return '11'

        if 3 == n:
            return '21'

        string = '21'
        n -= 3
        l_string = len(string)
        t_string = ''

        while n > 0:

            last = string[0]
            cur = 1
            count = 1
            while cur < l_string:

                if last == string[cur]:
                    count += 1
                else:
                    temp = str(count)
                    t_string += temp + last
                    last = string[cur]
                    count = 1
                cur += 1
            temp = str(count)
            t_string += temp + last
            string = t_string
            l_string = len(string)
            t_string = ''

            n -= 1
        return string

c = Solution()
d = c.countAndSay(6)
print(d)
















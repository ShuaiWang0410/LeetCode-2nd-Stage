'''
125 Valid Palindrome

简单的回文串判断,强化记忆
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        table = '1234567890'
        s_length = len(s)
        if s_length <= 1:
            return True

        pt1 = 0
        pt2 = s_length -1
        x_flag = False

        while True:

            if pt1 >= pt2:
                if x_flag:
                    return True
                elif pt1 == pt2:
                    return True
                else:
                    return False
            c1, c2 = s[pt1], s[pt2]
            if c1 not in table:
                c1 = ord(c1)
                if c1 < 97:
                    c1 += 32

                if c1 < 97 or c1 > 122:
                    pt1 += 1
                    continue

            if c2 not in table:
                c2 = ord(c2)
                if c2 < 97:
                    c2 += 32

                if c2 < 97 or c2 > 122:
                    pt2 -= 1
                    continue

            if c2 != c1:
                return False

            x_flag = True
            pt2 -= 1
            pt1 += 1


c = Solution()
print(c.isPalindrome("0p"))

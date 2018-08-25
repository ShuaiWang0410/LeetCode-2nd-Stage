'''
28. Implement strStr()

strStr(a,b)是一个函数，返回了b在a中最先出现的坐标

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0


        l_haystack = len(haystack)
        l_needle = len(needle)
        if l_haystack < l_needle:
            return -1
        start = False
        pos = -1
        pt1 = 0
        pt2 = 0



        while True:

            if pt1 == l_haystack:
                pos = -1
                break

            if haystack[pt1] != needle[pt2]:
                if not start:
                    pt1 += 1
                    continue
                else:
                    start = False
                    pt1 = pos + 1
                    pos = -1
                    pt2 = 0
                    continue
            else:
                if not start:
                    start = True
                    pos = pt1
                    if pt2 == l_needle - 1:
                        break
                    pt1 += 1
                    pt2 += 1
                else:
                    if pt2 == l_needle - 1:
                        break
                    else:
                        pt1 += 1
                        pt2 += 1



        return pos



c = Solution()
print(c.strStr("mississippi",
"issip"))



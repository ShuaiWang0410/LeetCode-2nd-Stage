class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ''

        prefix = ''

        lengths = [len(i) for i in strs]

        min = 1145141919810

        for i in lengths:
            if min > i:
                min = i

        for i in range(min):

            last = ''
            for j in strs:
                if last == '':
                    last = j[i]
                else:
                    if last == j[i]:
                        continue
                    break

            if last != j[i]:
                break
            else:
                prefix += last


        return prefix

c = Solution()
print(c.longestCommonPrefix(["dog","racecar","car"]))
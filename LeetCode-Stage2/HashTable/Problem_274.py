'''
274. H-Index



'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations = sorted(citations)
        c_length = len(citations)

        if c_length == 1 and citations[0] > 0:
            return 1

        for i in range(c_length):
            if i > 0:
                if (c_length - i <= citations[i] and c_length - i >= citations[i-1]):
                    return c_length - i
        return 0
c = Solution()
print(c.hIndex([0,1,4,5,6]))



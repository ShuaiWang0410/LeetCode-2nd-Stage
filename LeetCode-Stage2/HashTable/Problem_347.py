'''
347

'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        for i in nums:
            try:
                dic[i] = dic[i] + 1
            except KeyError:
                dic[i] = 1

        dic = sorted(dic.items(), key = lambda v:v[1], reverse=True)
        return [j[0] for j in dic][:k]

c = Solution()
d = c.topKFrequent([1,1,1,1,1,2,2,2,3,3,3,3], 2)
print(d)


'''
771. Jewels and Stones


'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        j_dict = {}
        for i in J:
            j_dict[i] = 1

        d = 0
        for i in S:
            try:
                if 1 == j_dict[i]:
                    d += 1
            except KeyError:
                continue

        return d

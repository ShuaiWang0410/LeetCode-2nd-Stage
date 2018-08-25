'''
167 Two Sum（Sorted）:
强化记忆
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        c_length = len(numbers)
        if c_length <= 1:
            return []

        pt1 = 0
        pt2 = c_length - 1
        while True:
            if pt1 >= pt2:
                break
            s = numbers[pt1] + numbers[pt2]
            if s > target:
                pt2 -= 1
                continue
            elif s < target:
                pt1 += 1
                continue
            else:
                return [pt1 + 1, pt2 + 1]

        return []
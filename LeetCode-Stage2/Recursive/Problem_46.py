'''
46. Permutation



'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        l_nums = len(nums)
        pattern = 0
        nums = sorted(nums)

        self.permuteR(nums, 0, [], permutations, l_nums, pattern)

        return permutations

    def permuteR(self, nums, depth, one_permutation, permutations, l_nums, pattern):

        if depth == l_nums:

            permutations.append(one_permutation)
            return

        else:

            for i in range(l_nums):

                t = pattern ^ (1 << i)

                if pattern > t:
                    continue
                else:
                    self.permuteR(nums, depth + 1, one_permutation + [nums[i]], permutations, l_nums, t)


c = Solution()
print(c.permute([1,2,3]))







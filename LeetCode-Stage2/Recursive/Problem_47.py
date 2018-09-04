'''
47 Permutation II

Deepin of 46

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
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
            last = ''

            for i in range(l_nums):

                t = pattern ^ (1 << i)

                if pattern > t:
                    continue
                else:
                    if last == nums[i]:
                        continue
                    else:
                        self.permuteR(nums, depth + 1, one_permutation + [nums[i]], permutations, l_nums, t)
                        last = nums[i]

c = Solution()
print(c.permute([1,1,2]))
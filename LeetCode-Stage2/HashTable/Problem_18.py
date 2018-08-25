'''
18 4 sum



'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        n_length = len(nums)

        if n_length < 4:
            return []

        answer_set = []
        last_i = ''
        last_j = ''

        print(nums)

        for i in range(0, n_length - 3):

            if nums[i] == last_i:
                continue

            last_j = ''

            for j in range(i + 1, n_length - 2):

                if nums[j] == last_j:
                    continue

                s_target = target - nums[i] - nums[j]

                p1 = j + 1
                p2 = n_length - 1
                while True:

                    if p1 >= p2:
                        break
                    if s_target - nums[p1] == nums[p2]:
                        answer_set.append([nums[i], nums[j], nums[p1], nums[p2]])
                        last = nums[p1]
                        while True:
                            p1 += 1
                            if nums[p1] > last or p1 == n_length - 1:
                                break

                    elif s_target - nums[p1] > nums[p2]:
                        p1 += 1
                    else:
                        p2 -= 1

                last_j = nums[j]

            last_i = nums[i]

        return answer_set

c = Solution()
d = c.fourSum( [-3,-2,-1,0,0,0,0,1,2,3], 0)
print(d)



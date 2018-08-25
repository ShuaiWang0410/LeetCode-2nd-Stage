class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        n_length = len(nums)
        if n_length < 3:
            return []

        answer_set = []
        last_i = ''


        for i in range(0, n_length - 2):

            if last_i == nums[i]:
                continue
            else:
                o_flag = ''

            pt1 = i + 1
            pt2 = n_length - 1

            last_pt1 = ''
            last_pt2 = ''

            target = 0 - nums[i]

            while True:
                if pt1 >= pt2:
                    break

                p1 = nums[pt1]
                p2 = nums[pt2]

                if last_pt1 == p1:
                    pt1 += 1
                    continue

                if last_pt2 == p2:
                    pt2 -= 1
                    continue

                s_target = p1 + p2
                if s_target == target:
                    answer_set.append([nums[i], p1, p2])
                    pt1 += 1
                    pt2 -= 1
                    last_pt2 = p2
                    last_pt1 = p1


                elif s_target > target:
                    pt2 -= 1
                else:
                    pt1 += 1

            last_i = nums[i]

        return answer_set
c = Solution()
print(c.threeSum([-1, 0, 1, 2, -1, -4]))
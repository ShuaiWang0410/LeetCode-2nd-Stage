'''
16. 3Sum Closest



'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        n_length = len(nums)

        if n_length <= 3:
            return sum(nums)

        dif = [nums[i] - nums[i-1] for i in range(1, n_length)]
        p1,p2,p = -1, -1, -1

        n_min = 1145141919810
        for i in range(n_length):

            min = 1145141919810
            pt1 = i + 1
            pt2 = n_length - 1
            s_target = target - nums[i]
            tp1, tp2, tp = -1, -1, -1
            while True:

                if pt1 >= pt2:
                    break

                n_dif = nums[pt1] + nums[pt2] - s_target

                if 0 == n_dif:
                    min = 0
                    tp, tp1, tp2 = i, pt1, pt2
                    break

                a_dif = abs(n_dif)

                if a_dif < min:
                    min = a_dif
                    tp, tp1, tp2 = i, pt1, pt2

                if n_dif * dif[pt1] < 0:
                    pt1 += 1
                else:
                    pt2 -= 1

            if min < n_min:
                n_min = min
                p, p1, p2 = tp, tp1, tp2
        return nums[p] + nums[p1] + nums[p2]

c = Solution()
d = c.threeSumClosest([1,2,4,8,16,32,64,128],82)
print(d)











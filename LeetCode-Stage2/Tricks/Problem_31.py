'''
31 Next Permutation

规律

找到一个排列的下一个，比如，1135的下一个排列是1153，1153的下一个排列是1315

规律：从最后一个向前找，找到第一个比自己小的数，交换，
     如果前面的数越来越大，那么找第一个改变这个趋势的数，比如572就是5，3521就是3，然后对这段（包含3）进行排序，找到第一个比3大的，将它提到前面

'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l_nums = len(nums)
        if 1 == l_nums:
            return
        if 2 == l_nums:
            temp = nums[0]
            nums[0] = nums[1]
            nums[1] = temp
            return

        pt = l_nums - 2
        start_flag = False
        while True:
            if nums[pt] == nums[pt + 1]:
                pt -= 1
                continue

            elif nums[pt] < nums[pt + 1]:
                if not start_flag:
                    temp = nums[pt]
                    nums[pt] = nums[pt + 1]
                    nums[pt + 1] = temp
                    break
                else:
                    pt2 = l_nums - 1
                    pt1 = nums[pt]
                    while True:

                        if nums[pt2] > pt1:
                            temp = nums[pt]
                            nums[pt] = nums[pt2]
                            nums[pt2] = temp
                            self.swap(nums, pt + 1, l_nums - 1)
                            break
                        pt2 -= 1
                    break


            else:
                if 0 == pt:
                    self.swap(nums, 0, l_nums - 1)
                    break

                start_flag = True
                pt -= 1

    def swap(self, nums, start, end):

        while True:
            if start >= end:
                break
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start += 1
            end -= 1

c = Solution()
nums = [1,3,2]
c.nextPermutation(nums)
print(nums)
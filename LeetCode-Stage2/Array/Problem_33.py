'''
33. Search in Rotated Sorted Array

二分

一个排好序的数组可能有某些原因进行了循环旋转如[0,1,2,4,5,6,7]转成了[4,5,6,7,0,1,2]
我们要做的是给定一个值，找这个值是否在数组中存在过，如果存在，则返回其下标，不存在，则返回-1。时间复杂度是O(log(n))

首先要找到这个旋转点，如[4,5,6,7,0,1,2]的旋转点是0

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l_nums = len(nums)
        if l_nums <= 5:
            for i in range(l_nums):
                if target == nums[i]:
                    return i
            return -1

        head = 0
        tail = l_nums - 1
        mnt = -1

        if nums[head] < nums[tail]:
            return self.biSearch(nums, head, tail, target)
        else:
            while True:

                mid = (head + tail) // 2
                if nums[mid] > nums[mid + 1]:
                    mnt = mid
                    break
                else:
                    if nums[mid] > nums[head]:
                        head = mid
                        continue
                    else:
                        tail = mid
                        continue

        if target >= nums[mnt + 1] and target <= nums[l_nums - 1]:
            if target == nums[mnt + 1]:
                return mnt + 1
            if target == nums[l_nums - 1]:
                return l_nums - 1
            return self.biSearch(nums, mnt + 1, l_nums - 1, target)
        else:
            if target == nums[0]:
                return 0
            if target == nums[mnt]:
                return mnt
            return self.biSearch(nums, 0, mnt, target)



    def biSearch(self, nums, start, end, target):
        while True:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if end <= start:
                return -1

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1


c = Solution()
print(c.search([150,151,152,156,158,159,160,161,162,167,169,170,171,177,180,183,184,186,189,191,197,200,203,205,210,215,216,219,221,222,233,236,237,238,239,246,247,250,254,257,260,261,262,269,275,279,283,284,286,287,288,289,290,294,295,298,1,5,6,9,10,13,15,16,20,25,27,28,34,37,41,42,43,46,47,48,51,53,54,59,61,65,67,72,76,78,79,81,83,85,91,92,94,95,102,103,105,106,111,113,118,120,122,123,126,141,148],48))
'''
Problem 88


'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        cur1 = 0
        cur2 = 0
        l_nums1 = len(nums1)
        l_nums2 = len(nums2)

        for i in range(n):
            nums1[m + i] = nums2[i]

        half = n/2
        x = m
        move = False
        for i in range(n):

            start = m - 1
            step = -1
            end_flag = False

            while True:
                if start == -1:
                    end_flag = True
                    break

                if nums2[i] >= nums1[start]:
                    break
                start += step
                move = True

            if move:
                temp = nums2[i]
                y = start - 1
                if end_flag:
                    y = -1
                    end_flag = False

                for j in range(m - 1, y, -1):
                    nums1[j + 1] = nums1[j]
                nums1[start] = temp
                move = False

            m += 1


c = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
c.merge(nums1, m, nums2, n)
print(nums1)










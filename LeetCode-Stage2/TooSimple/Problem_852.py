'''
852. Peak Index in a Mountain Array


'''

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        last = ''
        pos = 0
        l_A = len(A)
        for i in range(1, l_A):
            step = A[i] - A[i-1]
            if last == '':
                last = step
                continue
            if step < 0:
                if last > 0:
                    pos = i - 1
                    break
            else:
                last = step
                continue

        return pos

c = Solution()
print(c.peakIndexInMountainArray([1,2,3,2]))


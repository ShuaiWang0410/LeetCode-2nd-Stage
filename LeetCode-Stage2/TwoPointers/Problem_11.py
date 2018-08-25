'''
11


'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        h_length = len(height)

        if h_length <= 1:
            return 0

        pt1, pt2 = 0, h_length - 1

        max_vol = 0
        last_min = 0
        last_pt = -1

        while True:
            if pt1 >= pt2:
                break

            vol = 0
            width = pt2 - pt1
            if height[pt2] > height[pt1]:


                if last_pt == 1:
                    if last_min > height[pt1]:
                        pt1 += 1
                        continue
                last_pt = 1
                min = height[pt1]
                pt1 += 1

                vol = min * width

            else:

                if last_pt == 2:
                    if last_min > height[pt2]:
                        pt2 -= 1
                        continue
                last_pt = 2
                min = height[pt2] 
                pt2 -= 1

                vol = min * width

            if vol > max_vol:
                max_vol = vol
            last_min = min
        return max_vol

c = Solution()
d = c.maxArea([1,8,6,2,5,4,8,3,7])
print(d)



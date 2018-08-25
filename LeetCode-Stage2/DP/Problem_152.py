'''
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


IDEA:

(1)
因为是整形，如果不考虑负数只能越乘越大，所以一定是向后的方向
假设有两个变量v1,v2保存结果，v1保存只有正数的结果，v2保存正数和负数的结果
两个变量v1max 和v2max保存当前得到的最大结果
两个变量表示的子链的状态：v1可能是断开的，断开点之后到当前结果保存在v1中，之前的保存在v1max中 v2在遇到0前一定是连续的

这个思录错了，做到一半发现跟动规没关系

IDEA:

(2)
用动规的方法：


'''

'''

Solution1
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        v1, v2 = 0,0
        v1max = 0

        if 1 == len(nums):
            return nums[0]

        for i in nums:

            if i > 0:

                if 0 == v2:
                    v2 = i
                else:
                    v2 *= i

                if 0 == v1:
                    v1 = i
                else:
                    v1 *= i

                if v1 > v1max: v1max = v1;

            elif i < 0:

                if 0 == v2:
                    v2 = i
                else:
                    v2 *= i

                if v2 > 0:
                    v1max = v2
                    v1 = v2
                else:
                    v1max = v1
                    v1 = 0

            else:

                v2 = 0
                if v1 > v1max:
                    v1max = v1
                v1 = 0

        return v1max

'''

'''
Solution2

动规方法

状态转移方程为M[i][j] = max 

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxPos = -1145141919810
        maxNeg = 1
        pos = 0

        for i in nums:

            if i > 0:

                if pos == 0:
                    pos = i
                else:
                    pos *= i

                maxNeg *= i

            elif i < 0:

                maxNeg *= i

                if maxNeg > 0:
                            

            else:

                maxPos = max(maxPos, pos)
                pos = 0
                maxNeg = 0































# ------ EXECUTE PART ------

ins1 = Solution()

print(ins1.maxProduct([-2]))
print(ins1.maxProduct([2,-3,-2,4]))
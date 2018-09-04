'''
39 Combination Sum


'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        dp = [{} for i in range(candidates[0] + 1)]
        dp[candidates[0]][str(sorted([candidates[0]]))] = [candidates[0]]

        l_candidates = len(candidates)

        for i in range(candidates[0] + 1,target + 1):

            for j in range(l_candidates):

                r = i - candidates[j]
                t = candidates[j]
                if r < 0:
                    continue
                else:
                    if len(dp) == i:
                        dp.append({})
                    if 0 == r:
                        dp[i][str(sorted([t]))] = [t]
                    else:
                        if 0 != len(dp[r]):
                            for k in dp[r].values():
                                m = k + [t]
                                dp[i][str(sorted(m))] = m


        return list(dp[target].values())

c = Solution()
d = c.combinationSum([8,7,4,3],11)
print(d)







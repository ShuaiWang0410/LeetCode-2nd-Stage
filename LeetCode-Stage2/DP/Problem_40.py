'''
40. Combination Sum II

Deepin of 39



'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates = sorted(candidates)

        mark = 0
        for i in range(len(candidates) - 1, -1, -1):
            if target >= candidates[i]:
                mark = i
                break
        candidates = candidates[:mark + 1]

        sparse = {}
        sparse[-1] = -1
        l_candidates = len(candidates)
        for i in range(l_candidates):
            sparse[candidates[i]] = i
        answer_set = {}
        self.combinationSumR(sparse, l_candidates - 1, target, candidates, answer_set, [], l_candidates)
        return list(answer_set.values())




    def combinationSumR(self, sparse, end, target, candidates, answer_set, one_answer, l_candidates):

        if 0 == target:

            answer_set[str(sorted(one_answer))] = one_answer
            return

        else:
            pos = 0
            for i in range(target, -2, -1):
                try:
                    pos = sparse[i]
                    break
                except KeyError:
                    continue
            if -1 == pos:
                return
            if pos > end:
                pos = end

            for i in range(pos, -1, -1):

                temp = candidates[i]
                self.combinationSumR(sparse, i - 1, target - temp, candidates, answer_set, one_answer + [temp], l_candidates)


c = Solution()
d = c.combinationSum2([10,5],3)
print(d)











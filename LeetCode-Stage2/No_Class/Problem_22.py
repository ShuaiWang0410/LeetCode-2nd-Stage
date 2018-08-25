'''
22. Generate Parentheses

输入n，输出它的括号匹配

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]



'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if 0 == n:
            return []
        sets = []
        self.generator(sets, n-1, n, '(')
        return sets

    def generator(self, set, left, right, str):

        if left == 0:
            if right == 0:
                set.append(str)
                return
            else:
                self.generator(set, left, right-1, str + ")")
        else:
            self.generator(set, left - 1, right, str + "(")
            if right > left:
                self.generator(set, left, right - 1, str + ")")




c = Solution()
print(sorted(c.generateParenthesis(4)))
print(sorted(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]))






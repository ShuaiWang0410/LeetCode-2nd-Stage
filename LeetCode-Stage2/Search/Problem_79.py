'''
79. Word Search

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

应该是用BFS

'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        l_row = len(board)
        l_col = len(board[0])


        footprint = [[0 for i in range(l_col)] for j in range(l_row)]

        for i in range(l_row):
            for j in range(l_col):
                if word[0] == board[i][j]:
                    footprint[i][j] = 1
                    if self.DFS(i, j, footprint, board, word[1:], l_row - 1, l_col - 1):
                        return True
                    footprint[i][j] = 0
        return False




    def DFS(self, x, y, footprint, board, word, bx, by):

        if 0 == len(word):
            return True


        if x - 1 >= 0:
            if 0 == footprint[x-1][y]:
                if word[0] == board[x - 1][y]:
                    footprint[x-1][y] = 1
                    if self.DFS(x-1, y, footprint, board, word[1:], bx, by):
                        return True
                    footprint[x - 1][y] = 0

        if x + 1 <= bx:
            if 0 == footprint[x+1][y]:
                if word[0] == board[x + 1][y]:
                    footprint[x+1][y] = 1
                    if self.DFS(x+1, y, footprint, board, word[1:], bx, by):
                        return True
                    footprint[x + 1][y] = 0

        if y - 1 >= 0:
            if 0 == footprint[x][y - 1]:
                if word[0] == board[x][y - 1]:
                    footprint[x][y - 1] = 1
                    if self.DFS(x, y - 1, footprint, board, word[1:], bx, by):
                        return True
                    footprint[x][y - 1] = 0

        if y + 1 <= by:
            if 0 == footprint[x][y + 1]:
                if word[0] == board[x][y + 1]:
                    footprint[x][y + 1] = 1
                    if self.DFS(x, y + 1, footprint, board, word[1:], bx, by):
                        return True
                    footprint[x][y + 1] = 0

board = [
  ['A'],
  ['B'],
  ['C'],
  ['D']
]
c = Solution()
print(c.exist(board, "D"))




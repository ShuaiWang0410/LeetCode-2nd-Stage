'''
127. Word Ladder

hint

首先把这个问题转换成图的问题，那么问题就变成了，在图中找一条路径，使得终点为endWord

用DFS会超时，这里用BFS

'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        l_wordList = len(wordList)
        l_word = len(wordList[0])

        graph = [[0 for j in range(l_wordList)] for i in range(l_wordList)]

        for i in range(l_wordList):
            for j in range(i, l_wordList):
                count = 0
                w1 = wordList[i]
                w2 = wordList[j]
                for k in range(l_word):
                    if w1[k] == w2[k]:
                        count += 1
                if l_word - 1 == count:
                    graph[i][j] = 1
                    graph[j][i] = 1

        flag = False
        starts = []
        footPrint = [0 for j in range(l_wordList)]
        depth = []

        for i in range(l_wordList):
            count = 0
            w1 = beginWord
            w2 = wordList[i]
            for k in range(l_word):
                if w1[k] == w2[k]:
                    count += 1
            if l_word - 1 == count:
                flag = True
                starts.append(i)
                depth.append(2)
                footPrint[i] = 1

        if not flag:
            return 0


        return self.BFS(graph, wordList, endWord, starts, footPrint, l_wordList, depth)

    def BFS(self, graph, wordList, endWord, starts, footPrint, l_wordList, depth):

        if [] == starts:
            return 0

        head = starts[0]
        dep = depth[0]

        if endWord == wordList[head]:
            return dep

        else:
            for i in range(l_wordList):
                if graph[head][i] == 1:
                    if 1 != footPrint[i]:
                        if endWord == wordList[i]:
                            return dep + 1
                        starts.append(i)
                        depth.append(dep + 1)
                        footPrint[i] = 1


            return self.BFS(graph, wordList, endWord, starts[1:], footPrint, l_wordList, depth[1:])





'''

OLD SOLUTION (TIMEOUT)

    def DFS(self, i, graph, wordList, endWord, footPrint, l_wordList):

        if endWord == wordList[i]:
            footPrint[i] = 1
            return sum(footPrint)
        flag = False
        min = l_wordList
        for j in range(l_wordList):
            if 1 != footPrint[j]:
                if graph[i][j] == 1:
                    footPrint[j] = 1
                    temp = self.DFS(j, graph, wordList, endWord, footPrint, l_wordList)
                    if 0 != temp:
                        if min > temp:
                            flag = True
                            min = temp
                    footPrint[j] = 0
        if flag:
            return min
        return 0
'''


l = ["hot","dog","dot"]
c = Solution()
print(c.ladderLength("hot","dog",l))




'''
412. Fizz Buzz

被3整除叫做fizz，被5整除叫做buzz，同时被3和5整除的叫做fizzbuzz

Ace it.

'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        lastfizz = 3
        lastbuzz = 5

        answer = ["1",
    "2",
    "Fizz",
    "4",
    "Buzz",]

        if n <= 5:
            return answer[:n]


        for i in range(6, n + 1):
            if lastfizz == i - 3:
                if lastbuzz == i - 5:
                    answer.append("FizzBuzz")
                    lastbuzz = i
                    lastfizz = i
                    continue
                else:
                    answer.append("Fizz")
                    lastfizz = i
                    continue
            elif lastbuzz == i - 5:
                answer.append("Buzz")
                lastbuzz = i
                continue
            else:
                answer.append(str(i))
        return answer

c = Solution()
print(c.fizzBuzz(6))


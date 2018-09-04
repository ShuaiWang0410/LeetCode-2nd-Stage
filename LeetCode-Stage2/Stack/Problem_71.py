'''
Problem 71

Simplify the directory

/home/gm/ -> /home/gm
/home//gm -> /home/gm
/ab/./ -> /ab


'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = ['' for i in range(len(path) + 1)]
        stack[0] = 'end'

        l_path = len(path)
        head = 1
        cur = 0

        while True:

            if cur == l_path:
                break

            if path[cur] == "/":
                if 1 == head:
                    stack[head] = path[cur]
                    head += 1
                elif stack[head - 1] == "/":
                    cur += 1
                    continue
                elif stack[head - 1] == ".":
                    head -= 1
                    cur += 1
                    continue
                else:
                    stack[head] = path[cur]
                    head += 1

            elif path[cur] == ".":
                if stack[head - 1] == ".":
                    count = 0
                    head = head - 1
                    while True:
                        if stack[head - 1] == '/':
                            if stack[head - 2] == 'end':
                                break
                            if count == 1:
                                break
                            count += 1
                            head -= 1
                        else:
                            head -= 1
                else:
                    stack[head] = path[cur]
                    head += 1

            else:
                stack[head] = path[cur]
                head += 1


            cur += 1
        result = ''
        for i in range(1, head):
            result += stack[i]

        if result == "/":
            return "/"

        if result[-1] == ".":
            if result[-2] == "/" and len(result) > 2:
                return result[:-2]
            return result[:-1]

        if result[-1] == "/" or result[-1] == ".":
            return result[:-1]
        return result

c = Solution()
d = c.simplifyPath("/.")
print(d)





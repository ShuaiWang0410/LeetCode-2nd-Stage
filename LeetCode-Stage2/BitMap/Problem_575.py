'''
575. Distribute Candies

Ace it

'''

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        pmap = 0
        nmap = 0
        zmap = 0
        nsis = 0
        nbro = 0
        even = len(candies) // 2

        for i in candies:

            if even == nbro:
                pi = i
                if i < 0:
                    pi = -pi
                    pat = 1 << pi
                    if nmap < nmap ^ pat:
                        nsis += 1
                        nmap |= pat

                elif i == 0:
                    if zmap != 1:
                        zmap = 1
                        nsis += 1

                else:
                    pat = 1 << pi
                    if pmap < pmap ^ pat:
                        nsis += 1
                        pmap |= pat


                continue

            if even == nsis:
                return nsis

            pi = i
            if i < 0:
                pi = -pi
                pat = 1 << pi
                if nmap > nmap ^ pat:
                    nbro += 1
                else:
                    nmap |= pat
                    nsis += 1

            elif i == 0:
                if 1 == zmap:
                    nbro += 1
                else:
                    zmap = 1
                    nsis += 1
            else:
                pat = 1 << pi
                if pmap > pmap ^ pat:
                    nbro += 1
                else:
                    pmap |= pat
                    nsis += 1

        return nsis

c = Solution()
print(c.distributeCandies([100000,0,100000,0,100000,0,100000,0,100000,0,100000,0]))
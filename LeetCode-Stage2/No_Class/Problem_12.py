'''
12 Integer to Roman


'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        table = [
            ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["","X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["","M", "MM", "MMM"]
        ]

        if 0 == num:
            return ''
        str = ''
        for i in range(3,0,-1):
            base = pow(10,i)
            str += table[i][int(num / base)]
            num = num % base
        str += table[0][int(num)]

        return str

c = Solution()

print(c.intToRoman(45))


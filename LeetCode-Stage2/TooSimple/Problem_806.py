class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        lines = 0
        oneline = 0
        for i in S:

            if 0 == lines:
                lines += 1
            oneline += widths[ord(i) - 97]
            if oneline > 100:
                lines += 1
                oneline = widths[ord(i) - 97]
        return [lines, oneline]
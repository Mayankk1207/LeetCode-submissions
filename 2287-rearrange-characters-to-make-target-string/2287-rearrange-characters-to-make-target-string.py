class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        a = float("inf")
        seen = Counter(s)
        s = Counter(target)
        for x in target:
            a = min(a,seen[x]//s[x])
        return a
        
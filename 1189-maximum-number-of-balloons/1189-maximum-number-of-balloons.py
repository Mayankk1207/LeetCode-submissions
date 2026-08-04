from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        seen = Counter(text)
        s = Counter("balloon")
        a = float("inf")
        for x in "balloon":
            a = min(a,seen[x]//s[x])
        return a
                
        
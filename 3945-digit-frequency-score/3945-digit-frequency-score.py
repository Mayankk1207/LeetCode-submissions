from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        seen = Counter(str(n))
        c = 0

        for x in seen:
            c += int(x) * seen.get(x, 0)

        return c
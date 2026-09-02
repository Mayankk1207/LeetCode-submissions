from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        q = []
        res = ""
        seen = Counter(s)

        for x, y in seen.items():
            heapq.heappush(q, (-y, x))

        while q:
            i, j = heapq.heappop(q)
            res += (-i) * j

        return res


        
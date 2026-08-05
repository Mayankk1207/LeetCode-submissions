import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        lst = []
        for x in stones:
            heapq.heappush(lst,-x)
        while lst and len(lst) > 1:
            a = heapq.heappop(lst)
            b = heapq.heappop(lst)
            if a != b:
                heapq.heappush(lst, -abs(a-b))
            else:
                continue
        if not lst:
            return 0
        return abs(lst[0])


        
        
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def edu (x,y):
            return (x*x+y*y)**0.5
        lst = []
        res = []
        for x in points:
            dist = edu(x[0],x[1])
            heapq.heappush(lst,(dist,x[0],x[1]))
        for x in range(k):
            a,b,c = heapq.heappop(lst)
            res.append([b,c])
        return res
        

        
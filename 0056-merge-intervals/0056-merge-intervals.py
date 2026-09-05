class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        
        interval.sort(key = lambda x: x[0])
        res = [interval[0]]
        for i in range(1,len(interval)):
            if res[-1][1] >= interval[i][0]:
                res[-1][1] = max(res[-1][1],interval[i][1])
            else:
                res.append(interval[i])
        return res


        
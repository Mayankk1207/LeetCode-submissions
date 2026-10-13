import math
class Solution:
    def minEatingSpeed(self, piles: list[int], hr: int) -> int:
        i,j = 1,max(piles)
        while i <= j:
            h = 0 
            mid = i + ( j - i)//2
            for x in piles:
                h += math.ceil(float(x)/mid)
            if h <= hr:
                j = mid -1
            else:
                i = mid + 1
        return i

        
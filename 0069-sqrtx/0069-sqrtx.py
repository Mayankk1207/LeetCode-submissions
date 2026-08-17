class Solution:
    def mySqrt(self, x: int) -> int:
        i,j = 0,x
        while i<=j:
            mid = i + (j-i)//2
            sq = mid*mid
            if sq>x:
                j = mid-1
            elif sq<x:
                i = mid+1
            else:
                return mid
        return j
        
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l,r = max(nums),sum(nums)
        res = r
        def canwe(lar):
            subs = 1
            sum1 = 0 
            for x in nums:
                sum1 += x 
                if sum1 > lar:
                    sum1 = x
                    subs +=1
                if subs > k:
                    return False
            return True
        while l<=r:
            m = l + (r-l)//2
            if canwe(m):
                res = m 
                r = m -1
            else:
                l = m + 1
        return res
        

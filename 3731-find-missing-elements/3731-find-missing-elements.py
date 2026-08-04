class Solution(object):
    def findMissingElements(self, nums):
        seen = set(nums)
        a = min(nums)
        b = max(nums)
        res = []
        for x in range( a,b+1):
            if x not in seen:
                res.append(x)
        return res

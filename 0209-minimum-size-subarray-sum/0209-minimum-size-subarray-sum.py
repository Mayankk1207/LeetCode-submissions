class Solution(object):
    def minSubArrayLen(self, target, nums):
        ttl = 0
        res = float("inf")
        l,r = 0,0
        for x in nums:
            ttl+=x
            r+=1
            while ttl>=target:
                ttl -= nums[l]
                l+=1
                res = min(r-l,res)
        if res == float("inf"):
            return 0
        return res+1
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a,b = nums.index(max(nums)),nums.index(min(nums))
        p,r = max(a,b),min(a,b)
        q = (len(nums)-p) + r
        z =  len(nums)-r
        return min(p+1,q+1,z) 
        
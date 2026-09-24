class Solution:

    def smallestIndex(self, nums: List[int]) -> int:
        def helper(x):
            c = 0 
            while x>0:
                c+= x%10
                x//=10
            return c
        mix = float("inf")
        for i,j in enumerate(nums):
            if i == helper(j):
                mix = min(mix,i)
        if mix == float("inf"):
            return -1
        return mix
        

        
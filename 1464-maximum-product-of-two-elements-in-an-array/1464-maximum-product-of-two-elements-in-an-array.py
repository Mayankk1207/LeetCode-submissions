class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=j = 0
        for x in nums:
            if x>j:
                i = j 
                j = x
            elif x>i:
                i = x
        return (i-1)*(j-1)
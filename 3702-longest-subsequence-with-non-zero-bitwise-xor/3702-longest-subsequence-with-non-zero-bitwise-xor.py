class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for y in nums:
            x^=y
        if x != 0:
            return len(nums)
        for j in nums:
            if j != 0:
                return len(nums) - 1
        return 0 
        
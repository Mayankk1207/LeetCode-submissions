class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        s = max(nums)
        for x in nums:
            ans += s-x
        return ans
        
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: x**2)
        mid = len(nums)//2
        smaller = sum(x*x for x in nums[:mid])
        large = sum(x*x for x in nums[mid:])
        return large - smaller
        
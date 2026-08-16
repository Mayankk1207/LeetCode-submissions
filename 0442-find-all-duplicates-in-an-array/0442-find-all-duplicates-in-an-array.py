class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                res.append(abs(x))
            else:
                nums[i] *= -1
        return res
        
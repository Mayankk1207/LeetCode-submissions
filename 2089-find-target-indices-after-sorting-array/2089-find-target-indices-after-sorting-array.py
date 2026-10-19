class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res  = []
        for i,j in enumerate(sorted(nums)):
            if j == target:
                res.append(i)
        return res

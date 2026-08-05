class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        manx = float("inf")
        for i,j in enumerate(nums):
            if j == target:
                manx = min(manx,abs(i-start))
        return manx
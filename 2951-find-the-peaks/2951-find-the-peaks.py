class Solution(object):
    def findPeaks(self, nums):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                res.append(i)
        return res
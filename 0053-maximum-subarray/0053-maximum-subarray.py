class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        crr = m = nums[0]
        for i in range(1,len(nums)):
            crr = max(crr+nums[i],nums[i])
            m = max(crr,m)
        return m 
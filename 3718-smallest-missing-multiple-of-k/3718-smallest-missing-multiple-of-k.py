class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my = set(nums)
        for x in range(1,101):
            if x*k not in my:
                return x*k
        return (x+1)*k
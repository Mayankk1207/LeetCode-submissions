class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for x in nums:
            if x in seen:
                return x
            else:
                seen.add(x)
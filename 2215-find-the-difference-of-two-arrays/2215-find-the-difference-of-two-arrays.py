class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        seen1 = set(nums1)
        seen2 = set(nums2)
        res1 = []
        res2 = []
        for x in seen1:
            if x not in seen2:
                res1.append(x)
        for x in seen2:
            if x not in seen1:
                res2.append(x)
        return [res1,res2]

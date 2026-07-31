class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        return[x for x in nums if x < pivot] +[x for x in nums if x == pivot]+ [x for x in nums if x > pivot] 
        
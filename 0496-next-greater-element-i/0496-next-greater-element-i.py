class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums2)
        stc = []
        res2 = []
        for i in range(len(nums2)-1,-1,-1):
            while stc and stc[-1]<nums2[i]:
                stc.pop()
            if stc:
                res[i] = stc[-1]
            stc.append(nums2[i])
        for x in nums1:
            a = nums2.index(x)
            res2.append(res[a])
        return res2


        
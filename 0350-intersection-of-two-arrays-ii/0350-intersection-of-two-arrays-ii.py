from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        seen = Counter(nums1)
        for x in nums2:
            if x in seen and seen[x] > 0 :
                res.append(x)
                seen[x]-=1
        return res
        
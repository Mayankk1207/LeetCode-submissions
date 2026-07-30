class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        seen = [0]*(len(nums)+1)
        for i in nums:
            seen[i] +=1
        for i,j in enumerate(seen):
            if j == 2:
                res.append(i)
        return res
        
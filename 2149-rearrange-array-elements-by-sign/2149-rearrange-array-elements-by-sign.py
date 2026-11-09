class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p = [x for x in nums if x > 0]
        n = [ x for x in  nums if x <0]
        res = []
        for i in range(len(nums)//2):
            res.append(p[i])
            res.append(n[i])
        return res        
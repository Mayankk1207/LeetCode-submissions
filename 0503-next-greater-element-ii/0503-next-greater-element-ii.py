class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*(len(nums)*2)
        n = nums+nums
        stc = []
        for i in range(len(n)-1,-1,-1):
            while stc and stc[-1] <= n[i]:
                stc.pop()
            if stc:
                res[i] = stc[-1]
            stc.append(n[i])
        return res[:len(n)//2]

        
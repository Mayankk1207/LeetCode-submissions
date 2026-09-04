class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxA= []
        minA =[]
        maxm = nums[0]
        minm = nums[-1]
        ans = float("inf")
        for x in nums:
            if x > maxm:
                maxm = x
            maxA.append(maxm)
        for j in nums[::-1]:
            if j < minm:
                minm = j
            minA.append(minm)
        minA = minA[::-1]
        for i in range(len(nums)):
            ins =abs(maxA[i] - minA[i])
            if ins <= k:
                ans = min(ans,i)
        if ans == float("inf"):
            return -1
        return ans
            

        
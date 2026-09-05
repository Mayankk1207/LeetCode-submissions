class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxa = []
        mina = []
        i = nums[0]
        j = nums[-1]
        ans = float("inf")
        for x in nums:
            if x > i:
                i = x
            maxa.append(i)
        for x in nums[::-1]:
            if x < j:
                j = x 
            mina.append(j)
        mina = mina[::-1]

        for i in range(0,len(nums)):
            ins = abs(maxa[i] - mina[i])
            if ins <= k:
                ans = min(ans,i)
        if ans == float("inf"):
            return -1
        return ans


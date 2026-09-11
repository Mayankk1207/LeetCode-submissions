class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0:1}
        pre = 0 
        ans = 0
        for i in range(len(nums)):
            pre += nums[i]
            m = pre - goal
            ans += seen.get(m,0)
            seen[pre] =  seen.get(pre,0) + 1
        return ans

        
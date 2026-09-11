class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        pre = 0 
        ans = 0 
        for i in range(len(nums)):
            pre += nums[i]
            m = pre%k

            ans  += seen.get(m,0)
            seen[m] = seen.get(m,0) +1
        return ans
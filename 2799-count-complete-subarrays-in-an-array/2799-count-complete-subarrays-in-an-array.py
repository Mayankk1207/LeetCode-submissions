from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int: 
        s1 = Counter(nums)
        seen = {}
        l = 0 
        ans = 0 
        for r in range(len(nums)):
            seen[nums[r]] = 1 + seen.get(nums[r],0)
            while seen and len(seen) == len(s1):
                ans += len(nums) - r
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    seen.pop(nums[l])
                l+=1
        return ans
                


    



        
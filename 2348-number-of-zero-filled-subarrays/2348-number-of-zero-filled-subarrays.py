class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        s = 0
        ans = 0 
        for x in nums:
            if x == 0:
                s +=1
                ans +=s
            else:
                s = 0 
        return ans

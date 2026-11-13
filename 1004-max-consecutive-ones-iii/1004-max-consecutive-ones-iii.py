class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        z = 0 
        i = 0 
        ans = float("-inf")

        for j in range(len(nums)):
            if nums[j] == 0:
                z+=1
            while z > k:
                if nums[i] == 0:
                    z -=1
                i +=1
            ans = max(ans,j-i+1)
        return ans 
            
            




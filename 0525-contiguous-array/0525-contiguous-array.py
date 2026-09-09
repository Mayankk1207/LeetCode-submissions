class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0 
        seen= {0:-1}
        ans = 0 

        for i in range(len(nums)):

            if nums[i] == 0:
                pre -=1
            else:
                pre +=1
            
            if pre in seen:
                ans = max(ans, i - seen[pre])
            else:
                seen[pre] = i
        return ans 
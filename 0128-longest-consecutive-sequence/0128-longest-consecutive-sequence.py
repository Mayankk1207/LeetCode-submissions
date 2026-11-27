class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxm = 0
        seen = set(nums)
        cnt = 0 
        for x in seen:
            if x-1 not in seen:
                curr = x 
                cnt = 1
                while curr + 1 in seen:
                    curr +=1
                    cnt +=1
                maxm = max(cnt,maxm)
        return maxm
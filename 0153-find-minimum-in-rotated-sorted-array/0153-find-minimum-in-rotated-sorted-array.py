class Solution:
    def findMin(self, nums: list[int]) -> int:
        i,j = 0,len(nums)-1
        while(i<j):
            m = (i+j) //2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1 
        return nums[i]
        
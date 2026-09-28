class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        temp = [0]*len(nums)
        c = 0 
        for x in nums:
            if x%2==1:
                temp[c] = 1
                c+=1
        return temp[::-1]
        
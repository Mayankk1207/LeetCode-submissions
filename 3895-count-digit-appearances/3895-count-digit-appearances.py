class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        cnt = 0
        for x in nums:
            temp = x 
            while temp > 0:
                s = temp%10
                temp = temp//10
                if s == digit:
                    cnt +=1
        return cnt 
        
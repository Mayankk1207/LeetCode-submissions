class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0 
        f = y = 0 
        for x in nums:
            xor ^= x
        diff = xor & -xor
        for z in nums:
            if z & diff:
                f ^= z
            else:
                y ^= z 
        return [f,y]
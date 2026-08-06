class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while 1:
            temp = n
            p = 1
            while temp>0:
                p *= temp%10
                temp//=10
            if p%t==0 or p  == 0:
                return n
            else:
                n+=1
        
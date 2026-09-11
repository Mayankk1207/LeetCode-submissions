class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stc = []
        for x in num:
            while stc and k>0 and stc[-1] > x:
                stc.pop()
                k -=1
            stc.append(x)
        
        while k>0:
            stc.pop()
            k-=1
        
        res = "".join(stc).lstrip("0")

        return res if res else "0"
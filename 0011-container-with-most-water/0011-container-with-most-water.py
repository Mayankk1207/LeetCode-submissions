class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        i,j = 0,len(h) -1
        while i < j:
            w = j-i
            ans = max(ans,w*min(h[i],h[j]))
            if h[j] > h[i]:
                i+=1
            else:
                j-=1
        return ans 
        
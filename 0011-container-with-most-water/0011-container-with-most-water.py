class Solution:
    def maxArea(self, h: list[int]) -> int:
        i,j = 0,len(h)-1
        m = 0 
        ara = 0 
        while i<j:
            inx = min(h[i],h[j])
            ara = max(ara,inx*(j-i))
            if h[i]>=h[j]:
                j-=1
            else:
                i+=1
        return ara

        
        
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = {}
        maxL = 0
        maxf = 0 
        l,r = 0,0 
        for x in s:
            seen[x] = 1 + seen.get(x,0)
            maxf = max(maxf,seen[x])
            r+=1
            while (r-l)-maxf > k:
                seen[s[l]] -=1
                l+=1
            maxL = max(maxL,r-l+1)
        return maxL-1
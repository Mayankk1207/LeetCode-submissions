class Solution(object):
    def totalFruit(self, f):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l,seen,ans= 0,{},0

        for r in range(len(f)):
            seen[f[r]] = 1 + seen.get(f[r],0)
            while l<r and len(seen) >2:
                seen[f[l]] -= 1
                if seen[f[l]] == 0:
                    seen.pop(f[l])
                l+=1
            ans = max(ans,r-l+1)
        return ans 
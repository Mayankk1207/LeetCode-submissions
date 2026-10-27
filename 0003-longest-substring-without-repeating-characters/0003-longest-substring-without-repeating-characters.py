class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = float("-inf")
        i = 0
        if not s:
            return 0 
        for j in range(0,len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i +=1
            seen.add(s[j])
            ans= max(ans,j-i+1)
        return ans 



        
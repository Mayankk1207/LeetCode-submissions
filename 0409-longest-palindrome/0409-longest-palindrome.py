class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0 
        for x in s:
            if x in seen:
                seen.remove(x)
                ans+=2
            else:
                seen.add(x)
        if seen:
            ans+=1
        return ans

        
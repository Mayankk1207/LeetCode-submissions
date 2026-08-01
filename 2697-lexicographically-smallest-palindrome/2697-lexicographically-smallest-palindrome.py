class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        i,j = 0,len(s)-1
        while i<j:
            if s[i] == s[j]:
                res+=s[i]
            else:
                if s[i] < s[j]:
                    res+=s[i]
                else:
                    res+=s[j]
            i+=1
            j-=1
        if len(s)%2==0:
            return res+res[::-1]
        return res+s[len(s)//2] + res[::-1]        
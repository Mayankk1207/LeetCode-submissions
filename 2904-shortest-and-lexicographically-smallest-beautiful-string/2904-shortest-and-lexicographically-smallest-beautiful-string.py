class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        l,r = 0,0
        c = 0 
        res = ""
        for r in range(len(s)):
            if s[r] == "1":
                c+=1
            while c>k or (l<r and s[l]=="0"):
                if s[l] == "1":
                    c-=1
                l+=1
            if c==k:
                res1 = s[l:r+1]
                if res == "" or (len(res1)<len(res) or (len(res1)== len(res) and res1<res)):
                    res = res1
        return res





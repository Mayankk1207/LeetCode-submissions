class Solution:
    def checkValidString(self, s: str) -> bool:
        h = 0 
        l = 0 
        for x in s:
            if x =="(":
                h+=1
                l+=1
            if x == ")":
                h-=1
                l-=1
            if x == "*":
                l-=1
                h+=1
            l = max(l,0)
            if h <0:
                return False
        return l ==0 



        
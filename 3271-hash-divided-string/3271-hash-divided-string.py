class Solution(object):
    def stringHash(self, s, k):
        res = ""
        i = 0
        idx = len(s)//k
        for x in range(idx):
            he = 0 
            for _ in range(k):
                he += ord(s[i]) - ord("a")
                i+=1
            res += chr( he%26 + ord("a"))
            he = 0 
        return res 



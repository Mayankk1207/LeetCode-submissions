class Solution:
    def reverseDegree(self, s: str) -> int:
        s0 = 0 
        for i,j in enumerate(s):
            s0 += (ord("z") - ord(j) +1)*(i+1)
        return s0


        
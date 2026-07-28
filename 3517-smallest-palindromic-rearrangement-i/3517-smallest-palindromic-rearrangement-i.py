from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        res = ""
        seen = [0]*26
        for i in range(len(s)//2):
            seen[ord(s[i])-ord("a")] +=1
        for j in range(len(seen)):
            if seen[j] == 0:
                continue
            else:
                res1 = ""
                for y in range(seen[j]):
                    res1 += chr(j + ord("a"))
                res += res1
        if len(s) % 2 == 0:
            return res + res[::-1]
        elif len(s) == 1:
            return s
        else:
            return res + s[(len(s)//2)] + res [::-1]


        
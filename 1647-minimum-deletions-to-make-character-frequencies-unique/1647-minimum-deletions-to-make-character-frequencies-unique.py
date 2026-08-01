from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen1 = Counter(s)
        seen = set()
        res = 0 
        for x in seen1.values():
            if x not in seen:
                seen.add(x)
            else:
                i = 1
                while x-i>0 and x-i in seen:
                    i+=1
                res+=i
                seen.add(x-i)
        return res
            




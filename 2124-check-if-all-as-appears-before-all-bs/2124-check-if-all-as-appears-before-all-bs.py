class Solution(object):
    def checkString(self, s):
        cnt = 0
        for x in s:
            if x == "a" and cnt == 0:
                continue
            if x == "b":
                if cnt == 0:
                    cnt +=1
                continue
            if x == "a" and cnt == 1:
                return False
        return True
            
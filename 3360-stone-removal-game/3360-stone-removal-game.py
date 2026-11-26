class Solution(object):
    def canAliceWin(self, n):
        cnt = 0
        stones = 10

        while n >= stones:
            n -= stones
            stones -= 1
            cnt += 1

        return cnt % 2 == 1
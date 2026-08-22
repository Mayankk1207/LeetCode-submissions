class Solution(object):
    def checkDivisibility(self, n):
        temp = n 
        sumq = 0 
        multi = 1

        while n > 0:
            d = n % 10
            sumq = sumq + d
            multi = multi * d
            n = n // 10

        return temp%(sumq+multi) == 0 
        
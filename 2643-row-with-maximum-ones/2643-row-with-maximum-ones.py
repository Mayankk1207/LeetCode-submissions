class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        i = 0 
        s = 0 

        for i,j in enumerate(mat):
            temp = sum(j)
            if temp > s:
                s = temp
                ind = i
        
        return [ind,s]


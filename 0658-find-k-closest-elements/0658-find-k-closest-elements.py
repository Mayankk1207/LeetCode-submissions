class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        a,b = 0,len(arr)-1
        while b-a+1>k:
            if abs(arr[a]-x) > abs(arr[b]-x):
                a+=1
            else:
                b-=1
        return arr[a:b+1]

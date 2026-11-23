class ProductOfNumbers(object):

    def __init__(self):
        self.pre = [1]
        

    def add(self, num):
        if num == 0:
            self.pre = [1]
        else:
            self.pre.append(self.pre[-1]*num)
    

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = len(self.pre)
        if k>= n :
            return 0 
        else:
            return self.pre[-1] // self.pre[n-k-1]
    
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
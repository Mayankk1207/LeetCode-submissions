class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [-1]*k
        self.size = 0 
        self.s = 0 
        self.r = 0
        self.k = k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.q[self.r] = value
        self.r = (self.r+1)%self.k
        self.size +=1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        res = self.q[self.s]
        self.s = (self.s+1)%self.k
        self.size -=1
        return True
        

    def Front(self):
        if self.isEmpty():
            return -1 
        return self.q[self.s]
        
    def Rear(self):
        if self.isEmpty():
            return -1 
        return self.q[(self.r-1)%self.k]
        

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class FreqStack(object):

    def __init__(self):
        self.maps = {}
        self.mxc = 0
        self.stcs = {}
        

    def push(self, val):
        inx = 1 + self.maps.get(val,0)
        self.maps[val] = inx
        if self.mxc < inx:
            self.stcs[inx] = []
            self.mxc = inx
        self.stcs[inx].append(val)        

    def pop(self):
        res = self.stcs[self.mxc].pop()
        self.maps[res] -=1
        if not self.stcs[self.mxc]:
            self.mxc -=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
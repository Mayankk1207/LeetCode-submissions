class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        else:
            he = self.mp[key]
            i,j = 0,len(he)-1
            ans = ""
            while(i<=j):
                mid = (i+j)//2
                if he[mid][1] == timestamp:
                    return he[mid][0]
                if he[mid][1] < timestamp:
                    ans = he[mid][0]
                    i = mid +1
                else:
                    j = mid -1
            return ans


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
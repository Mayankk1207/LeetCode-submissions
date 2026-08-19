class Solution:
    def largestRectangleArea(self, hts: List[int]) -> int:
        stc = []
        arr = 0
        for i,j in enumerate(hts):
            if not stc or stc[-1][1] <= j:
                stc.append([i,j])
            else:
                while stc and stc[-1][1] > j:
                    idx,val = stc.pop()
                    arr = max(arr,(i-idx)*val)
                stc.append([idx,j])
        for x,y in stc:
            arr = max(arr,(len(hts)-x)*y)
        return arr

                
class Solution:
    def carFleet(self, target: int, posn: List[int], speed: List[int]) -> int:
        arr = []
        for x in range(len(posn)):
            temp = (target-posn[x])/speed[x]
            arr.append([posn[x],temp])
        arr.sort(key = lambda x: x[0],reverse = True)
        stack = []
        for x in arr:
            if not stack:
                stack.append(x)
            elif stack[-1][1] >= x[1]:
                continue
            else:
                stack.append(x)
        return len(stack)
        
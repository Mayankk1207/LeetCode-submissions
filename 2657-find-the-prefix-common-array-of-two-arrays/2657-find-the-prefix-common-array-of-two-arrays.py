class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen1 = set()
        seen2 = set()
        res = []
        for i in range(len(A)):
            seen1.add(A[i])
            seen2.add(B[i])
            res.append(len(seen1&seen2))
        return res

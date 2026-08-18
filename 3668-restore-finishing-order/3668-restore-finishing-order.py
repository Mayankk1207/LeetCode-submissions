class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        seen = set(friends)
        res = []
        for x in order:
            if x in seen:
                res.append(x)
        return res
class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for x in s:
            if x == "i":
                res = res[::-1]
            else:
                res.append(x)
        return "".join(res)
        
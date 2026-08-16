class Solution:
    def decodeString(self, s: str) -> str:
        stc = []
        for x in s:
            if x != "]":
                stc.append(x)
            else:
                cr = ""
                k = ""
                while stc and stc[-1] != "[":
                    cr=stc.pop() + cr
                stc.pop()
                while stc and stc[-1].isdigit():
                    k = stc.pop() + k
                stc.append(int(k)*cr)
        return "".join(stc)
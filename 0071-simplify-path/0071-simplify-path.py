class Solution:
    def simplifyPath(self, s: str) -> str:
        stc = []
        for x in s.split("/"):
            if x == "..":
                if stc:
                    stc.pop()
            elif x == "." or x == "":
                continue
            else:
                stc.append(x)
        return "/" + "/".join(stc)            
                   
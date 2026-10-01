class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stc.append(x)
            else:
                if len(stc) == 0:
                    return False
                elif x == "]" and stc[-1] == "[":
                    stc.pop()
                elif x == "}" and stc[-1] == "{":
                    stc.pop()
                elif x == ")" and stc[-1] == "(":
                    stc.pop()

                else:
                    return False
        
        return len(stc) == 0 
        
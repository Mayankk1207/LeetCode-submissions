class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        rex = []
        while a or b:
            if a > b:
                rex.append("a")
                a-=1

                if a > b:
                    rex.append("a")
                    a-=1
                if b:
                    rex.append('b')
                    b-=1
            else:
                rex.append("b")
                b-=1
                if a < b:
                    rex.append("b")
                    b-=1
                if a:
                    rex.append('a')
                    a-=1
        return "".join(rex)
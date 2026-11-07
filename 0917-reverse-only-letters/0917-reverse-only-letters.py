class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        string = list(s)
        i,j = 0,len(string)-1
        while i<j:
            if string[i].isalpha() and string[j].isalpha():
                string[i],string[j] = string[j],string[i]
                i+=1
                j-=1
            else:
                while i<j and not string[i].isalpha():
                    i+=1
                while i <j and  not  string[j].isalpha():
                    j-=1
        return "".join(string)

        
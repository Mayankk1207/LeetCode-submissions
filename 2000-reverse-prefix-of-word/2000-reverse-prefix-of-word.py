class Solution(object):
    def reversePrefix(self, word, ch):
        stc = []
        if ch not in word:
            return word
        for i,x in enumerate(word):
            stc.append(x)
            if x == ch:
                break
        return  "".join(stc[::-1]) + word[i+1:]
            
        
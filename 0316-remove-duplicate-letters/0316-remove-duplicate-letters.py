from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        count = Counter(s)
        stack = []
        seen = set()
        for x in s:
            count[x] -=1

            if x in seen:
                continue
            
            while stack and stack[-1] > x and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(x)
            seen.add(x)
        return "".join(stack)
            
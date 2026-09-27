class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
            
        return "".join(res)

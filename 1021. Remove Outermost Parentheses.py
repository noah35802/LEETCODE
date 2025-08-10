class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        for c in s:
            if c == '(':
                if depth > 0:
                    res.append('(')
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(')')
        return ''.join(res)

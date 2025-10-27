class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets:
                if not stack or stack[-1] != brackets[i]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {']': '[', ')': '(', '}': '{'}

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
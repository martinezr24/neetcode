class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c_to_o = {"}": "{", ")": "(", "]": "["}

        for b in s:
            if b in c_to_o:
                if stack and stack[-1] == c_to_o[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if len(stack) == 0:
            return True
        return False


        
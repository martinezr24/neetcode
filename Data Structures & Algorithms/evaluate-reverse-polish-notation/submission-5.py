class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(int(tokens[i]))
            else:
                l = stack.pop()
                sl = stack.pop()

                if tokens[i] == "+":
                    stack.append(l + sl)
                elif tokens[i] == "-":
                    stack.append(sl - l)
                elif tokens[i] == "*":
                    stack.append(l * sl)
                elif tokens[i] == "/":
                    stack.append(int(sl / l))

        return stack[-1]
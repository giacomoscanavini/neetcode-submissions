class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time complexity: Loop over the tokens O(n)
        # Space complexity: Create the stack O(n)
        stack = []
        for c in tokens:
            if c == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))

        return stack.pop()
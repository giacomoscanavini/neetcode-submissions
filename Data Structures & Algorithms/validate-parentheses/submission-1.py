class Solution:
    def isValid(self, s: str) -> bool:
        # Time complexity: Loop over each element of s O(n)
        # Space complexity: Create a stack up to n/2 elements O(n)
        stack = []
        open_br = set(['(', '[', '{'])
        close_br = set([')', ']', '}'])
        for c in s:
            if c in open_br: stack.append(c)
            else:
                if len(stack) > 0:
                    if c == ')': 
                        if stack[-1] == '(': stack.pop(-1)
                        else: return False
                    elif c == ']':
                        if stack[-1] == '[': stack.pop(-1)
                        else: return False
                    else:
                        if stack[-1] == '{': stack.pop(-1)
                        else: return False
                else:
                    return False
                
        if len(stack) == 0: return True
        else: return False
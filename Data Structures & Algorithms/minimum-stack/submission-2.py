class MinStack:
    # Time complexity: All operations occur in O(1)
    # Space complexity: Create two stacks O(n)
    def __init__(self):
        self.stack = []
        self.prefix_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0: 
            self.min_val = val
        else:
            self.min_val = min(self.prefix_stack[-1], val)
        self.stack.append(val)
        self.prefix_stack.append(self.min_val)
        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.prefix_stack.pop(-1)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_stack[-1]
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minNum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)

        self.minNum = min(val, self.minNum)
        self.minStack.append(self.minNum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minNum = self.minStack[-1] if self.minStack else float("inf")

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

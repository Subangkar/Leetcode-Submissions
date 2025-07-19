class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min)>0:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)
        

    def pop(self) -> None:
        # if len(self.min)==0:
        #     return
        self.stk.pop()
        self.min.pop()

    def top(self) -> int:
        # if len(self.min)==0:
        #     return
        return self.stk[-1]

    def getMin(self) -> int:
        # if len(self.min)==0:
        #     return None
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
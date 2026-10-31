class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_val=float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        else:
            if val < self.min_val:
                encoded= 2*val - self.min_val
                self.stack.append(encoded)
                self.min_val = val
            else:
                self.stack.append(val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.min_val:
            self.min_val = 2 * self.min_val - top
    
        

    def top(self) -> int:
        x=self.stack[-1]
        if x< self.min_val:
            return self.min_val
        return x
        

    def getMin(self) -> int:
        return self.min_val
        

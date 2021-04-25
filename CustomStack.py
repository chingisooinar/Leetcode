class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None for _ in range(maxSize)]
        self.ptr = 0
        self.len = maxSize
    def push(self, x: int) -> None:
        if self.ptr != self.len:
            self.stack[self.ptr] = x
            self.ptr += 1
    def pop(self) -> int:
        if self.ptr != 0:
            val = self.stack[self.ptr - 1]
            self.stack[self.ptr - 1] = None
            self.ptr -= 1
            return val
        return -1 
    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < self.len and self.stack[i]:
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

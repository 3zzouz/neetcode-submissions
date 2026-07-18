from collections import deque
class MinStack:
    def __init__(self):
        self.array: deque[int] = deque([])
        self.min_to_curr : deque[int] = deque([])
        self.count = 0

    def push(self, val: int) -> None:
        if self.count == 0:
            self.min_to_curr.append(val)
        else :
            self.min_to_curr.append(min(self.getMin(),val))
        self.count += 1
        self.array.append(val)


    def pop(self) -> None:
        self.count -= 1
        self.min_to_curr.pop()
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_to_curr[-1]

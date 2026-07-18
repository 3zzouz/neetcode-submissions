from heapq import heapify,heappop
from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = [(-position[i],speed[i]) for i in range(len(position))]
        heapify(pos)
        (x,v) = heappop(pos)
        t = (target + x)/v
        res = deque([t])
        while pos:
            (x,v) = heappop(pos)
            t = (target + x)/v
            if t > res[-1]: res.append(t)
        return len(res)
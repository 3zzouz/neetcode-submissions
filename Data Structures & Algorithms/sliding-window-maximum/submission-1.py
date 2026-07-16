from heapq import heapify,heappushpop, heappop
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i]=-nums[i]
        s = 0
        res=deque([])
        while s+k-1 < n:
            window = nums[s:s+k]
            heapify(window)
            m = heappop(window)
            res.append(-m)
            s+=1
        return list(res)

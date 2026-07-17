from heapq import heapify,heappushpop, heappop,heappush
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            nums[i]=-nums[i]
        s = 0
        res=deque([])
        window = [(e,i) for i,e in enumerate(nums[:k])]
        heapify(window)
        deleted = set()
        while s+k-1 < n:
            while deleted and window and window[0] in deleted:
                deleted.remove(window[0])
                heappop(window)
            m = window[0]
            res.append(-m[0])
            deleted.add((nums[s],s))
            s+=1
            end = s+k-1
            if end < n : heappush(window,(nums[end],end))  
        return list(res)

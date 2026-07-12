import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):return 0
        heapq.heapify(nums)
        prefix = heapq.heappop(nums)
        nb = 1
        maxS = 1
        for _ in range(len(nums)):
            new = heapq.heappop(nums)
            if new == prefix : continue
            if new == prefix +1 :
                nb +=1
            else :
                maxS = max(nb,maxS)
                nb = 1
            prefix = new
        return max(nb,maxS)
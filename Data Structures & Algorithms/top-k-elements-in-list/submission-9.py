import heapq
from collections import defaultdict,deque
class Solution:
    class Element:
        def __init__(self, occurence: int,value:int):
            self.occurence = occurence
            self.value=value
        # Define how 'less than' works for this class
        def __lt__(self, other: Element) -> bool:
            return self.occurence < other.occurence 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tas = []
        dic : dict[int,int] = defaultdict(int)
        res = deque([])
        for el in nums:
            dic[el]+=1
        for val,occ in dic.items():
            heapq.heappush(tas,self.Element(occ,val))
            if len(tas)>k:
                heapq.heappop(tas)
        for i in range(k):
            res.append(heapq.heappop(tas).value)
        return list(res)

            
        
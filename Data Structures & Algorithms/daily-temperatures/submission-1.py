from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        aux = deque([])
        for i,e in enumerate(temperatures):
            while aux and aux[-1][1] < e:
                res[aux[-1][0]] = i - aux[-1][0]
                aux.pop()
            aux.append((i,e))
        return list(res)
            
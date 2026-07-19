from collections import deque, defaultdict
class TimeMap:

    def __init__(self):
        self.ma : dict[str,deque[tuple[int,str]]] = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ma[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.ma[key]
        n = len(array)
        if n ==0 : return ''
        l = 0
        r = n - 1
        while l<r-1 :
            mil = int((l+r)/2)
            if array[mil][0] == timestamp : return array[mil][1]
            if array[mil][0] > timestamp:
                r = mil - 1
            else:
                l = mil
        if array[r][0] <= timestamp:
            return array[r][1]
        if array[l][0] <= timestamp:
            return array[l][1]
        return ''
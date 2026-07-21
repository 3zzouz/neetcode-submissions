class Node :
    def __init__(self, val :int = 0,key :int = 0,next:"Node | None" = None,prev:"Node | None" = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.idx : dict[int,Node] = {}
        self.first_element = Node()
        self.last_element = self.first_element
        self.count = capacity
    def place_node_at_end(self,el:Node):
        nex = el.next if el else None
        prev = el.prev if el else None

        if nex and prev :
        #if not last element => make it
            prev.next = nex
            nex.prev = prev
            if self.last_element:
                self.last_element.next = el
            el.prev = self.last_element
            el.next = None
            self.last_element = el
    def get(self, key: int) -> int:
        if not key in self.idx :
            return -1
        
        el = self.idx[key]
        self.place_node_at_end(el)

        return el.val if el else -1

    def put(self, key: int, value: int) -> None:
        if key in self.idx :
            el = self.idx[key]
            el.val = value
            self.place_node_at_end(el)
        else:
            if self.count == 0:
                if self.first_element and self.first_element.next :
                    el = self.first_element.next
                    nex = el.next
                    self.first_element.next = nex
                    if nex:
                        nex.prev = self.first_element
                    k = el.key
                    del el
                    del self.idx[k]
                    self.count += 1
            new = Node(next=None,key=key,val=value,prev=self.last_element)
            self.idx[key] = new
            if self.last_element:                
                self.last_element.next = new
            self.last_element = new
            self.count -= 1

from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idx = defaultdict(tuple)
        curr = head
        while curr:
            idx[curr] = (Node(curr.val),curr.next,curr.random)
            curr = curr.next
        for v in idx.values() :
            n = v[1]
            r = v[2]
            v[0].next = idx[n][0] if n else None
            v[0].random = idx[r][0] if r else None
        return idx[head][0] if head else None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        aux = deque([root])
        res = deque([root.val])
        while aux:
            n = len(aux)
            for _ in range(n):
                el = aux.popleft()
                if el:
                    if el.left : aux.append(el.left)
                    if el.right : aux.append(el.right)
            if aux:
                res.append(aux[-1].val)
        return list(res)
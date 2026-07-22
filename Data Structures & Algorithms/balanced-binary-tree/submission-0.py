# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self) -> None:
        self.idx:dict[Optional[TreeNode],int] = {None:0}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.idx[root.left] = left
        self.idx[root.right] = right
        curr = max(self.idx[root.left],self.idx[root.right])+1
        self.idx[root] = curr
        return curr
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        queue : deque[Optional[TreeNode]] = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                el = queue.popleft()
                l = self.idx[el.left if el else None]
                r = self.idx[el.right if el else None]
                if abs(l-r)>1:
                    return False
                if el : 
                    queue.append(el.left)
                    queue.append(el.right)
        return True

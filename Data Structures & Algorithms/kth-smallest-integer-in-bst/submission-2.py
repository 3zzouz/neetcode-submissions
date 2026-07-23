# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        aux = -1
        def dfs(root:TreeNode):
            nonlocal k
            nonlocal aux
            if root.left : 
                dfs(root.left)
                k-=1
            if k==1:
                aux = root.val
                return 
            if root.right :
                k-=1
                dfs(root.right)
        dfs(root)
        return aux

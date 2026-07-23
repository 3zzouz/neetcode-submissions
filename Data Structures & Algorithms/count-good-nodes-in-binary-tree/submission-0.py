# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        def dfs(root:Optional[TreeNode],m:int):
            nonlocal count
            if not root:
                return
            aux = max(m,root.val)
            dfs(root.left,aux)
            dfs(root.right,aux)
            if root.val == aux:
                count+=1
        dfs(root.left,root.val)
        dfs(root.right,root.val)
        return count

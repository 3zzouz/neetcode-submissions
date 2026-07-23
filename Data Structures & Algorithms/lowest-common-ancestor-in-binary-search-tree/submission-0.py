# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root :
            return None
        lowest = min(p.val if p else 101,q.val if q else 101)
        biggest = max(p.val if p else -101,q.val if q else -101)
        if lowest <= root.val and biggest >= root.val:
            return root
        if biggest <= root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if lowest >= root.val:
            return self.lowestCommonAncestor(root.right,p,q)
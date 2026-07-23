# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root:Optional[TreeNode],mini:int | None=None,maxi:int|None=None)-> bool:
            if not root:
                return True
            if mini is not None and root.val <= mini:
                return False
            if maxi is not None and root.val >= maxi:
                return False
            return dfs(root.right,mini=root.val,maxi=maxi) and dfs(root.left,mini=mini,maxi=root.val)
        return dfs(root,None,None)
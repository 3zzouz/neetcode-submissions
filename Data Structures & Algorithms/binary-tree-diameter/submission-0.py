# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.idx : dict[Optional[TreeNode],int] = {None : 0}
        self.m : int = 0
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
    def recursivediameterOfBinaryTree(self,depth ,root: Optional[TreeNode]):
        if not root:
            return
        score_left = self.idx[root.left]
        score_right = self.idx[root.right]
        l = [score_right+score_left,score_left+depth,score_right+depth]
        m = max(l)
        self.m = max(self.m,m)
        self.recursivediameterOfBinaryTree(depth+1,root.right)
        self.recursivediameterOfBinaryTree(depth+1,root.left)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        self.recursivediameterOfBinaryTree(0,root)
        return self.m
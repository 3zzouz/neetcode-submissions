# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = deque([p])
        q1 = deque([q])
        while p1:
            n = len(p1)
            for i in range(n):
                el1 = p1.popleft()
                el2 = q1.popleft()
                v1 = el1.val if el1 else None
                v2 = el2.val if el2 else None
                if v1 != v2:
                    return False
                if el1:
                    p1.append(el1.left)
                    p1.append(el1.right)
                if el2:
                    q1.append(el2.left)
                    q1.append(el2.right)

        return True
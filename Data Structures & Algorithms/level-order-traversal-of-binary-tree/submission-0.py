# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque([root])
        ret = deque([])
        while res:
            n = len(res)
            aux = deque([])
            for _ in range(n):
                el = res.popleft()
                if el:
                    aux.appendleft(el)
                    if el.right : res.append(el.right)
                    if el.left : res.append(el.left)
            if aux : ret.append([el.val for el in aux])
        return list(list(i) for i in ret)


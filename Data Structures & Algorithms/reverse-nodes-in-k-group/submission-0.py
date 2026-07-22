# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        oldprev = None
        res = first = last = head
        isFirst = True
        while last:
            n = k
            while n:
                if not last:
                    return res
                last = last.next
                n-=1
            prev = last
            curr = first
            while not curr is last:
                tmp = curr.next
                curr.next =prev
                prev = curr
                curr = tmp
            if oldprev:
                oldprev.next = prev
            oldprev = first
            first = curr
            if isFirst:
                res = prev
                isFirst = False
        return res

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def inverseList(self,l:Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = l
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        res = curr
        r = 0
        while l1 or l2:
            s = r
            if l1:
                s+=l1.val
                l1 = l1.next
            if l2:
                s+=l2.val
                l2 = l2.next
            d = s % 10
            curr.next = ListNode(d)
            curr = curr.next
            r = s // 10
        if r :
            curr.next = ListNode(r)
            curr = curr.next
        return res.next            
            

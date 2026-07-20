# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next : return None
        fast = head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        prev = None
        slow = head
        while fast and slow:
            fast = fast.next

            prev = slow
            slow = slow.next
        if prev :
            if slow:
                prev.next = slow.next
        else :
            return slow.next if slow else None
        return head
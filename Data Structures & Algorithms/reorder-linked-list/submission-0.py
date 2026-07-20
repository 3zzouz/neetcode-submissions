from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Edge case: empty list or single node requires no reordering
        if not head or not head.next:
            return

        # 1. Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next and slow and slow.next:
            slow = slow.next     # Move 1 step
            fast = fast.next.next  # Move 2 steps (Crucial fix!)

        # 2. Split the list and reverse the second half
        # 'slow' is at the middle. 'curr' starts the second half.
        curr: Optional[ListNode] = slow.next
        slow.next = None  # Sever the connection between halves (Crucial fix!)
        
        prev: Optional[ListNode] = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # 3. Merge the two halves alternatingly
        first: Optional[ListNode] = head
        second: Optional[ListNode] = prev  # Head of the reversed second half
        
        while second and first:
            # Safely store next nodes before changing pointers
            tmp1, tmp2 = first.next , second.next
            
            # Link nodes
            first.next = second
            second.next = tmp1
            
            # Advance pointers for next iteration
            first = tmp1
            second = tmp2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self,l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
        dummy = ListNode(val=-1001,next=l1)
        l1 = dummy
        while l2:
            while l1 and l1.next and l1.next.val <= l2.val:
                l1 = l1.next
            v1 = l1.val if l1 else 1001
            v2 = l2.val if l2 else 1001
            l1next = l1.next if l1 else None
            l2next = l2.next
            if l1 : l1.next = l2
            l2.next = l1next
            l2 = l2next
            l1 = l1.next if l1 else None
        res = dummy.next
        del dummy
        return res
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(len(lists)-1):
            lists[i+1] = self.mergeTwoLists(lists[i],lists[i+1])
        return lists[-1] if len(lists) > 0 else None
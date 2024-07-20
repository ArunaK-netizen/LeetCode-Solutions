# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        if (head is None or head.next is None):
            return head
        while (i and i.next is not None):
            if (i.val == i.next.val):
                i.next = i.next.next
            else:
                i = i.next
        return head

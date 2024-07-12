# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        prev = i.val
        i = i.next
        zeroth_link = head
        while i is not None:
            if (i.val != 0):
                i.val = prev + i.val
                prev = i.val
                zeroth_link.next = i
            else:
                prev = i.val
                zeroth_link = i
            i = i.next

        i = head
        head = i.next
        while i.next is not None:
            if ((i.next).val == 0):
                i.next = (i.next).next
            else:
                i = i.next
        return head





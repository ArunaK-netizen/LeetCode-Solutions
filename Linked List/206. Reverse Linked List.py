# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = None
        while (temp1 is not None):
            next_node = temp1.next
            temp1.next = temp2
            temp2 = temp1
            temp1 = next_node
        head = temp2
        return head

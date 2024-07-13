# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head.next is None):
            return None
        length = 0
        i = head
        while (i is not None):
            i = i.next
            length += 1
        currentIndex = 0
        i = head
        while (i is not None):
            if (currentIndex + 1 == length // 2):
                nextNode = i.next.next
                i.next = nextNode
            currentIndex += 1
            i = i.next
        return head

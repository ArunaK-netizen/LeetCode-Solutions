# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        i = head
        while (i is not None):
            length += 1
            i = i.next
        middle = length // 2
        i = head
        currentIndex = 0
        while (currentIndex != middle):
            currentIndex += 1
            i = i.next
        return i

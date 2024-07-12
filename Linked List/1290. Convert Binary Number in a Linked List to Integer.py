# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        i = head
        while (i is not None):
            i = i.next
            length += 1
        decimal = 0
        currentIndex = 0
        i = head
        while (i is not None):
            decimal += 2 ** (length - currentIndex - 1) * i.val
            currentIndex += 1
            i = i.next
        return decimal

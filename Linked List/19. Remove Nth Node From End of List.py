# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(head):
            i = head
            countNodes = 0
            while (i is not None):
                i = i.next
                countNodes += 1
            return countNodes

        i = head
        totalNodes = length(head)
        if (totalNodes - n == 0):
            return head.next
        currentIndex = 0
        while (i is not None):
            if (currentIndex + 1 == totalNodes - n):
                i.next = i.next.next
            currentIndex += 1
            i = i.next
        return head

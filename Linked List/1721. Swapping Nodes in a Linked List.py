# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        swapValue = 0
        n = 0
        i = head
        while (i is not None):
            n += 1
            i = i.next

        first = head
        currentIndex = 0
        while (first is not None):
            if (currentIndex == k - 1):
                break
            first = first.next
            currentIndex += 1

        second = head
        currentIndex = 0
        while (second is not None):
            if (currentIndex == n - k):
                break
            second = second.next
            currentIndex += 1

        first.val, second.val = second.val, first.val
        return head

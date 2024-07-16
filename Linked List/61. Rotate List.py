# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        def length(head):
            countNodes = 0
            i = head
            while i is not None:
                i = i.next
                countNodes += 1
            return countNodes

        n = length(head)
        k = k % n
        if k == 0:
            return head

        i = head
        while i.next is not None:
            i = i.next
        i.next = head

        i = head
        currentIndex = 0
        while currentIndex < n - k - 1:
            i = i.next
            currentIndex += 1

        new_head = i.next
        i.next = None

        return new_head
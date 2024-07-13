# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Reverse the linked list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        head = reverse(head)
        stack = []
        result = []

        while head:
            while stack and stack[-1] <= head.val:
                stack.pop()
            if not stack:
                result.append(0)
            else:
                result.append(stack[-1])
            stack.append(head.val)
            head = head.next

        return result[::-1]

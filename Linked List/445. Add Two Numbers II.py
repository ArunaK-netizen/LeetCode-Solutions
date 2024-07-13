# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            length = 0
            temp1 = head
            temp2 = None
            while (temp1 is not None):
                nextNode = temp1.next
                temp1.next = temp2
                temp2 = temp1
                temp1 = nextNode
                length += 1
            head = temp2
            return head, length

        l1, lenOne = reverse(l1)
        l2, lenTwo = reverse(l2)
        if (lenOne > lenTwo):
            i = l1
            j = l2
        else:
            i = l2
            j = l1
        carry = 0
        while (i is not None or j is not None):
            if (i is not None and j is not None):
                value = i.val + j.val + carry
                i.val = value % 10
                value = value // 10
                carry = value
                i = i.next
                j = j.next
            else:
                value = i.val + carry
                i.val = value % 10
                value = value // 10
                carry = value
                i = i.next

        if (lenOne > lenTwo):
            head, length = reverse(l1)
            if (carry != 0):
                node = ListNode(carry)
                node.next = head
                head = node
            return head
        head, length = reverse(l2)
        if (carry != 0):
            node = ListNode(carry)
            node.next = head
            head = node
        return head

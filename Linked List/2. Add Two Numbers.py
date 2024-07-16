# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            i = head
            countNodes = 0
            while (i is not None):
                i = i.next
                countNodes += 1
            return countNodes

        if (length(l1) > length(l2)):
            head = l1
            i = l1
            j = l2
        else:
            head = l2
            i = l2
            j = l1

        carry = 0
        while (i is not None):
            if (j is not None):
                value = i.val + j.val + carry
                i.val = value % 10
                carry = value // 10
                j = j.next
            else:
                break
            i = i.next

        while (i is not None):
            value = i.val + carry
            i.val = value % 10
            carry = value // 10
            i = i.next
        if (carry == 0):
            return head
        else:
            i = head
            while (i.next is not None):
                i = i.next
            i.next = ListNode(carry)
            return head

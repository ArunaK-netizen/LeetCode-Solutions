# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            temp1 = head
            temp2 = None
            while (temp1 is not None):
                nextNode = temp1.next
                temp1.next = temp2
                temp2 = temp1
                temp1 = nextNode
            head = temp2
            return head

        carry = 0
        head = reverse(head)
        i = head
        while (i is not None):
            temp = i.val
            value = (i.val * 2) % 10
            i.val = value + carry
            carry = (temp * 2) // 10
            i = i.next
        if (carry == 0):
            return reverse(head)
        else:
            head = reverse(head)
            firstNode = ListNode(carry)
            firstNode.next = head
            head = firstNode
            return head




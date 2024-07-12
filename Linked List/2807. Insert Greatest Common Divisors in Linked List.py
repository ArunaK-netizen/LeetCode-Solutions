# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if (b == 0):
                return a
            else:
                return gcd(b, a % b)

        i = head
        while (i.next is not None):
            temp = i.next
            node = ListNode(gcd(i.val, (i.next).val))
            i.next = node
            node.next = temp
            i = temp
        return head

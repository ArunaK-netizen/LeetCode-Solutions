# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head1):
            temp1 = head1
            temp2 = None
            while (temp1 is not None):
                next_node = temp1.next
                temp1.next = temp2
                temp2 = temp1
                temp1 = next_node
            head1 = temp2
            return head1

        head = reverse(head)
        i = head
        maxRL = i.val

        while (i.next is not None):

            if (i.next.val < maxRL):
                i.next = i.next.next
            else:

                maxRL = max(maxRL, i.next.val)
                i = i.next

        return reverse(head)

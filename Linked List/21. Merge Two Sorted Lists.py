# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if (list1 is None and list2 is None):
            return None

        elif (list1 is None and list2 is not None):
            return list2

        elif (list1 is not None and list2 is None):
            return list1

        if (list1.val < list2.val):
            i = list1
            j = list2
        else:
            i = list2
            j = list1
        head = i
        while (i.next is not None):
            if (j and j.val <= i.next.val):
                nextNode = i.next
                jNextNode = j.next
                i.next = j
                j.next = nextNode
                j = jNextNode
            i = i.next
        if (j):
            i.next = j
        return head

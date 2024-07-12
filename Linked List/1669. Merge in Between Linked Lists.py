# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = list1
        currentIndex = 0
        while (currentIndex != b):
            if (currentIndex == a - 1):
                first = i

            i = i.next
            currentIndex += 1

        merge = i.next
        first.next = list2
        j = list2
        while (j.next is not None):
            j = j.next
        j.next = merge
        return list1

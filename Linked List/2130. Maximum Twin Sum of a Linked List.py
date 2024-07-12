# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        i = head
        while (i is not None):
            i = i.next
            n += 1

        first = head
        second = head
        currentIndex = 0
        while (second is not None):
            if (currentIndex == n // 2 - 1):
                secondHead = second.next
                second.next = None
                break
            second = second.next
            currentIndex += 1

        temp1 = secondHead
        temp2 = None
        while temp1 is not None:
            next_node = temp1.next
            temp1.next = temp2
            temp2 = temp1
            temp1 = next_node
        secondHead = temp2

        maxPairSum = 0
        i = head
        j = secondHead
        while (i is not None):
            if (i.val + j.val > maxPairSum):
                maxPairSum = i.val + j.val
            i = i.next
            j = j.next
        return maxPairSum

        return 0

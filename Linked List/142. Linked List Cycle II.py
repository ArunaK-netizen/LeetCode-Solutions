# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = dict()
        currentIndex = 0
        i = head
        while (i is not None):
            if (i not in visited):
                visited[i] = currentIndex
            else:
                return i
            i = i.next
        return None

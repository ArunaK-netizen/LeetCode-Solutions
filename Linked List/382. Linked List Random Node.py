# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = self.head
        length = 0
        while (i is not None):
            i = i.next
            length += 1
        randomIndex = random.randrange(0, length)
        currentIndex = 0
        i = self.head
        while (currentIndex != randomIndex):
            i = i.next
            currentIndex += 1
        return i.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
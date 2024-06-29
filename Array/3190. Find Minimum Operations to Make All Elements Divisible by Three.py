class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        countOperations = 0
        for i in nums:
            if (i % 3 != 0):
                countOperations += 1
        return countOperations

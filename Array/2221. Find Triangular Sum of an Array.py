class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        def calculateTriangle(arr):
            currentLevel = []
            for i in range(len(arr) - 1):
                currentLevel.append((arr[i] + arr[i + 1]) % 10)
            return currentLevel

        modified = nums
        for i in range(len(nums) - 1):
            modified = calculateTriangle(modified)
        return modified[0]


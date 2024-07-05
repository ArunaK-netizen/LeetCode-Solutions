class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumSquares = 0
        n = len(nums)

        for i in range(1, len(nums) + 1):
            if (n % i == 0):
                sumSquares += nums[i - 1] ** 2
        return sumSquares

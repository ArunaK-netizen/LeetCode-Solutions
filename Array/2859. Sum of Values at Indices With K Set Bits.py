class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def countSetBits(n):
            count = 0
            while n != 0:
                n = n & (n - 1)
                count += 1
            return count

        sumElements = 0
        for i in range(len(nums)):
            t = countSetBits(i)
            if (k == t):
                sumElements += nums[i]
        return sumElements


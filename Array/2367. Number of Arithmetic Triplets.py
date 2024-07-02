class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set()
        count = 0
        for i in nums:
            if ((i - diff) in nums and (i + diff) in nums):
                count += 1

        return count

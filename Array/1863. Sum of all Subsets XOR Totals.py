class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def subsets(nums, res, subset, index):
            res.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                subsets(nums, res, subset, i + 1)
                subset.pop(-1)
            return

        res = []
        subset = []
        index = 0
        subsets(nums, res, subset, index)
        xorTotal = 0
        for i in res:
            xor = 0
            for j in i:
                xor ^= j
            xorTotal += xor

        return xorTotal

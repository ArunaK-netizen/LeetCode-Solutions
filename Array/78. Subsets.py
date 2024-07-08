class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generateSub(arr, res, subset, index):
            res.append(subset[:])
            for i in range(index, len(arr)):
                subset.append(arr[i])
                generateSub(arr, res, subset, i + 1)
                subset.pop(-1)

        res = []
        subset = []
        index = 0
        generateSub(nums, res, subset, index)
        return res 
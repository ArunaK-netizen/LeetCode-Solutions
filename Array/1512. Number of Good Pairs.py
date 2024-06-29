class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        countDict = {}
        setNums = list(set(nums))
        for i in range(len(setNums)):
            countDict[setNums[i]] = nums.count(setNums[i])
        count = 0
        for i in countDict:
            count += countDict[i] * (countDict[i] - 1) // 2
        return count


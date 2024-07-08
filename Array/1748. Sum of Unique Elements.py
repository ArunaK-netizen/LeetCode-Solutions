class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        countDict = Counter(nums)
        answer = 0
        for i in countDict:
            if (countDict[i] == 1):
                answer += i
        return answer

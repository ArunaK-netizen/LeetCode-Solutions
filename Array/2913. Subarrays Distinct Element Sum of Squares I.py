class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0

        for i in range(len(nums)):
            temp = 0
            for j in range(i + 1, len(nums) + 1):
                temp += len(set(nums[i:j])) ** 2
            answer += temp
        return answer


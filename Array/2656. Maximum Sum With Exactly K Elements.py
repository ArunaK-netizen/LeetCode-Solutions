class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(max(nums), max(nums) + k):
            answer += i
        return answer

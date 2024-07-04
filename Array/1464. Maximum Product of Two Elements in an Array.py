class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 1
        answer *= max(nums) - 1
        nums.pop(nums.index(max(nums)))
        answer *= max(nums) - 1
        return answer


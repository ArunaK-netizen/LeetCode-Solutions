class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxPairSum = 0
        for i in range(len(nums) // 2):
            s = nums[i] + nums[len(nums) - i - 1]
            if (s > maxPairSum):
                maxPairSum = s
        return maxPairSum



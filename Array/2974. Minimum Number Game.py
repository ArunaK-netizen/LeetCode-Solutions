class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        i = 0
        while (i < len(nums)):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        return nums

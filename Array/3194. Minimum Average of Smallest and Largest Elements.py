class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average = []
        nums = sorted(nums)
        while (len(nums) != 0):
            average.append((nums[0] + nums[-1]) / 2)
            nums.pop(0)
            nums.pop(-1)

        return min(average)

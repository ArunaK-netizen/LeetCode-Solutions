class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            element = nums[i]
            reverse = 0
            while element != 0:
                reverse = reverse * 10 + element %10
                element = element // 10
            nums.append(reverse)
        print(nums)
        return len(set(nums))

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def calDigitSum(num):
            s = 0
            while(num!=0):
                s += num % 10
                num = num // 10
            return s
        elementSum = sum(nums)
        digitSum = 0
        for i in nums:
            digitSum += calDigitSum(i)
        return abs(elementSum - digitSum)